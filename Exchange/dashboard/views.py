from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render
from wallet.models import Token, Wallet
from .forms import BuyForm, SellForm


@login_required
def home(request):
    tokens = Token.objects.all()

    actual_price = Token.objects.get(name="bitcoin").actual_price
    user_pk = request.user.pk
    token_quantity = Wallet.objects.get(owner=user_pk, token=1).quantity

    if request.method == "POST":
        buy_form = BuyForm(request.POST)
        if buy_form.is_valid():
            messages.success(request, f"its work ")

    else:
        buy_form = BuyForm()

    return render(request, 'dashboard/home.html', {'title': 'Dashboard',
                                                   'subtitle': 'Home',
                                                   'tokens': tokens,
                                                   'price': actual_price,
                                                   'form': buy_form,
                                                   'quantity': token_quantity})
