from django.contrib import admin
from .models.wallet import Wallet
from .models.token import Token
from .models.history import History

admin.site.register(Wallet)
admin.site.register(Token)
admin.site.register(History)
