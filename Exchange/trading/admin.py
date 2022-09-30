from django.contrib import admin
from .models import WithdrawalDepositHistory, TradingHistory

admin.site.register(TradingHistory)
admin.site.register(WithdrawalDepositHistory)
