from django.contrib import messages
from django.http import HttpRequest
from wallet.models.wallet import Wallet
from wallet.models.token import Token
from .get_core_information import get_core_information
from .save_transaction_history import save_trading_history


def sell_now(context: dict, request: HttpRequest, actual_price: float, token_pk: int) -> dict:

    exchange_pk, usdt_pk, transaction_fee = get_core_information()

    form = context['form']
    amount_buyer = float(form.data['amount'])
    transaction_price = actual_price * amount_buyer - transaction_fee
    user_token_wallet = context['user_token_wallet']
    user_usdt_wallet = context['user_usdt_wallet']
    exchange_token_wallet = Wallet.objects.get(owner=exchange_pk, token=token_pk)
    exchange_usdt_wallet = Wallet.objects.get(owner=exchange_pk, token=usdt_pk)

    if form.is_valid() and amount_buyer <= user_token_wallet.quantity:

        if transaction_price <= exchange_usdt_wallet.quantity:
            user_token_wallet.quantity = user_token_wallet.quantity - amount_buyer
            user_usdt_wallet.quantity = user_usdt_wallet.quantity + transaction_price

            exchange_token_wallet.quantity = exchange_token_wallet.quantity + amount_buyer
            exchange_usdt_wallet.quantity = exchange_usdt_wallet.quantity - transaction_price

            user_token_wallet.save()
            user_usdt_wallet.save()
            exchange_token_wallet.save()
            exchange_usdt_wallet.save()

            context['user_token_wallet'] = user_token_wallet
            context['user_usdt_wallet'] = user_usdt_wallet

            token = Token.objects.get(pk=token_pk)

            save_trading_history(user=request.user,
                                 token=token,
                                 quantity=amount_buyer,
                                 transaction_type='sell',
                                 transaction_price=transaction_price)

            messages.success(request, f"You sell  {amount_buyer} {token.symbol}  for  {transaction_price} USDT")
        else:
            messages.error(request, extra_tags="danger",
                           message=f"The operation can not be completed - stock exchange doesn't have the resources")
    else:
        messages.warning(request, f"The operation can not be completed - You are too poor")

    return context
