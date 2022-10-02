from wallet.models.wallet import Wallet
from typing import Union


def get_user_balance(user_pk: int) -> Union[int, list]:
    user_wallets = Wallet.objects.filter(owner=user_pk)
    wallet_values = []
    user_balance = 0

    for wallet in user_wallets:
        value = wallet.quantity * wallet.token.actual_price
        user_balance += value
        wallet_values.append(round(value, 2))

    return round(user_balance, 2), wallet_values, user_wallets
