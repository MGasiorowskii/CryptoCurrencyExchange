from django.db import models
from wallet.models.token import Token
from django.contrib.auth.models import User


class TransactionHistory(models.Model):
    token = models.ForeignKey(Token, on_delete=models.CASCADE)
    quantity = models.FloatField(default=0.0, blank=False)
    date_time = models.DateTimeField(blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.TextField(blank=False)

    def __str__(self):
        return f"{self.user} {self.type} {self.quantity} {self.token}"

    class Meta:
        abstract = True


class TradingHistory(TransactionHistory):
    transaction_price = models.FloatField(blank=False)


class WithdrawalDepositHistory(TransactionHistory):
    address = models.FloatField(blank=True)
