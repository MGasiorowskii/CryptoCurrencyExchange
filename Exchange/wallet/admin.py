from django.contrib import admin
from .models import Wallet, Token, History

admin.site.register(Wallet, Token, History)
