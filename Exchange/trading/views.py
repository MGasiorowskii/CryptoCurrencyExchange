from django.http import HttpRequest
from wallet.models.token import Token
from wallet.models.wallet import Wallet
from .forms import BuySellForm
from django.views.generic.detail import DetailView
from dashboard.utils import create_plot
from trading.operations.buy_now import buy_now
from trading.operations.sell_now import sell_now
from trading.operations.get_core_information import get_core_information
from trading.operations.get_history_transaction import get_token_history_transaction


class TokenDetailView(DetailView):
    model = Token
    template_name = "trading/token.html"
    slug_field = 'name'

    def get_context_data(self, request, **kwargs):
        context = super().get_context_data(**kwargs)

        _, usdt_pk, _ = get_core_information()

        user_pk = request.user.pk
        user_token_wallet = Wallet.objects.get(owner=user_pk, token=self.object.pk)
        user_usdt_wallet = Wallet.objects.get(owner=user_pk, token=usdt_pk)
        context['history'] = get_token_history_transaction(token_pk=self.object.pk)

        context['form'] = BuySellForm()
        context['user_token_wallet'] = user_token_wallet
        context['user_usdt_wallet'] = user_usdt_wallet
        context['tokens'] = Token.objects.all()
        context['title'] = self.object.name.capitalize()
        context['graph'] = create_plot(samples=500, token_id=self.object.pk)
        return context

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(request=request, object=self.object)
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(request=request, object=self.object)
        context['form'] = BuySellForm(request.POST)

        context = self.form_validation(context, request)

        return self.render_to_response(context)

    def form_validation(self, context: dict, request: HttpRequest) -> dict:

        if 'sell_token' in request.POST:
            context = sell_now(context=context,
                               request=request,
                               actual_price=self.object.actual_price,
                               token_pk=self.object.pk)

        elif 'buy_token' in request.POST:
            context = buy_now(context=context,
                              request=request,
                              actual_price=self.object.actual_price,
                              token_pk=self.object.pk)

        return context
