from django.db import models
from django.contrib.auth.models import User
from .token import Token


class Wallet(models.Model):
    token = models.ForeignKey(Token, on_delete=models.CASCADE)
    quantity = models.FloatField(default=0.0, blank=False)
    address = models.TextField(blank=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Wallet of {self.owner} - {self.token}"
