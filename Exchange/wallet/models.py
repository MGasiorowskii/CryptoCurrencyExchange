from django.db import models
from django.contrib.auth.models import User


class Token(models.Model):
    name = models.TextField(blank=False)
    symbol = models.TextField(max_length=10, blank=False)
    actual_price = models.FloatField(blank=False)

    def __str__(self):
        return f"{self.name}"


class Wallet(models.Model):
    token = models.OneToOneField(Token, on_delete=models.CASCADE)
    quantity = models.FloatField(blank=False)
    address = models.TextField(blank=False)
    owner = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Wallet of {self.owner} - {self.token}"


class History(models.Model):
    token = models.ForeignKey(Token, on_delete=models.CASCADE)
    price = models.FloatField()
    date_time = models.DateTimeField(blank=False)

    def __str__(self):
        return f"History of {self.token} - {self.date_time}"
