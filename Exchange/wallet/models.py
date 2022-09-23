from django.db import models
from django.contrib.auth.models import User


class Token(models.Model):
    name = models.CharField(blank=False)
    symbol = models.TextField(max_length=10, blank=False)
    actual_price = models.FloatField(blank=False)

    def __str__(self):
        return f"{self.name}"


class Wallet(models.Model):
    token = models.OneToOneField(Token, on_delete=models.CASCADE)
    quantity = models.FloatField(blank=False)
    address = models.CharField(blank=False)
    owner = models.OneToOneField(User, on_delete=models.CASCADE)


class History(models.Model):
    token = models.OneToOneField(Token, on_delete=models.CASCADE)
    price = models.FloatField()
    date_time = models.DateTimeField(unique=True, blank=False)

    def __str__(self):
        return f"History of {self.token} - {self.date_time}"
