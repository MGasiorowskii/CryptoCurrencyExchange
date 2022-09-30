from ..models import TradingHistory
from django.contrib.auth.models import User
from wallet.models.token import Token
import datetime
import pytz


def save_trading_history(user: User, token: Token, quantity: float, transaction_type: str, transaction_price: float) -> None:
    date_time = datetime.datetime.now(tz=pytz.UTC)

    TradingHistory.objects.create(token=token,
                                  quantity=quantity,
                                  date_time=date_time,
                                  user=user,
                                  type=transaction_type,
                                  transaction_price=transaction_price)
