from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render
from wallet.models import Token, Wallet
from .forms import BuySellForm
from django.views.generic.detail import DetailView


EXCHANGE_PK = 13
USDT_PK = 3
TRANSACTION_FEE = 5


@login_required
def home(request):
    form = BuySellForm()
    tokens = Token.objects.all()
    token_actual_price = Token.objects.get(name="bitcoin").actual_price

    user_pk = request.user.pk
    user_token_wallet = Wallet.objects.get(owner=user_pk, token=1)
    user_usdt_wallet = Wallet.objects.get(owner=user_pk, token=USDT_PK)
    user_token_quantity = user_token_wallet.quantity
    user_usdt_quantity = user_usdt_wallet.quantity

    exchange_token_wallet = Wallet.objects.get(owner=EXCHANGE_PK, token=1)
    exchange_usdt_wallet = Wallet.objects.get(owner=EXCHANGE_PK, token=USDT_PK)
    exchange_token_quantity = exchange_token_wallet.quantity
    exchange_usdt_quantity = exchange_usdt_wallet.quantity

    if request.method == "POST":
        if 'buy_token' in request.POST:
            form = BuySellForm(request.POST)
            token_actual_price = Token.objects.get(name="bitcoin").actual_price

            amount_buyer = float(form.data['amount'])
            transaction_price = token_actual_price * amount_buyer + TRANSACTION_FEE

            if form.is_valid() and transaction_price <= user_usdt_quantity:

                if amount_buyer <= exchange_token_quantity:
                    user_token_wallet.quantity = user_token_quantity + amount_buyer
                    user_usdt_wallet.quantity = user_usdt_quantity - transaction_price

                    exchange_token_wallet.quantity = exchange_token_quantity - amount_buyer
                    exchange_usdt_wallet.quantity = exchange_usdt_quantity + transaction_price

                    user_token_wallet.save()
                    user_usdt_wallet.save()
                    exchange_token_wallet.save()
                    exchange_usdt_wallet.save()

                    user_usdt_quantity = user_usdt_wallet.quantity
                    user_token_quantity = user_token_wallet.quantity

                    messages.success(request, f"You bought {amount_buyer} BTC")
                else:
                    messages.error(request, f"The operation can not be completed - stock exchange doesn't have the resources")
            else:
                messages.warning(request, f"The operation can not be completed - You are too poor")

        elif 'sell_token' in request.POST:
            form = BuySellForm(request.POST)
            token_actual_price = Token.objects.get(name="bitcoin").actual_price

            amount_buyer = float(form.data['amount'])
            transaction_price = token_actual_price * amount_buyer + TRANSACTION_FEE

            if form.is_valid() and amount_buyer <= user_token_quantity:

                if transaction_price <= exchange_usdt_quantity:
                    user_token_wallet.quantity = user_token_quantity - amount_buyer
                    user_usdt_wallet.quantity = user_usdt_quantity + transaction_price

                    exchange_token_wallet.quantity = exchange_token_quantity + amount_buyer
                    exchange_usdt_wallet.quantity = exchange_usdt_quantity - transaction_price

                    user_token_wallet.save()
                    user_usdt_wallet.save()
                    exchange_token_wallet.save()
                    exchange_usdt_wallet.save()

                    user_usdt_quantity = user_usdt_wallet.quantity
                    user_token_quantity = user_token_wallet.quantity

                    messages.success(request, f"You sell {amount_buyer} BTC")
                else:
                    messages.error(request, f"The operation can not be completed - stock exchange doesn't have the resources")
            else:
                messages.warning(request, f"The operation can not be completed - You are too poor")

    return render(request, 'dashboard/home.html', {'title': 'Dashboard',
                                                   'subtitle': 'Home',
                                                   'tokens': tokens,
                                                   'price': token_actual_price,
                                                   'form': form,
                                                   'user_usdt_quantity': user_usdt_quantity,
                                                   'user_token_quantity': user_token_quantity})


class TokenDetailView(DetailView):
    model = Token
    template_name = "dashboard/token.html"

    def get_context_data(self, request, **kwargs):
        context = super().get_context_data(**kwargs)

        user_pk = request.user.pk
        user_token_wallet = Wallet.objects.get(owner=user_pk, token=self.object.pk)
        user_usdt_wallet = Wallet.objects.get(owner=user_pk, token=USDT_PK)
        context['form'] = BuySellForm()
        context['user_token_wallet'] = user_token_wallet
        context['user_usdt_wallet'] = user_usdt_wallet
        return context

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(request=request, object=self.object)
        return self.render_to_response(context)

