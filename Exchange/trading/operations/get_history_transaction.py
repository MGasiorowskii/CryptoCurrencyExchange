from ..models import TradingHistory


def get_history_transaction(token_pk: int, user_pk: int) -> list[TradingHistory]:

    history = TradingHistory.objects.filter(token=token_pk, user=user_pk)
    return history


def get_token_history_transaction(token_pk: int) -> list[TradingHistory]:

    history = TradingHistory.objects.filter(token=token_pk)
    return history


def get_user_history_transaction(user_pk: int) -> list[TradingHistory]:

    history = TradingHistory.objects.filter(user=user_pk)
    return history
