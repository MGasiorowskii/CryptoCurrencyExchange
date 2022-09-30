from wallet.models.token import Token
from django.contrib.auth.models import User


EXCHANGE_PK = 13
USDT_PK = 3
TRANSACTION_FEE = 5


def get_core_information() -> list[int]:
    """Return information about exchange PK, USDT token PK and transaction fee"""

    usdt_token = Token.objects.get(name='tether')
    exchange_object = User.objects.get(username='Exchange')

    return exchange_object.pk, usdt_token.pk, TRANSACTION_FEE
