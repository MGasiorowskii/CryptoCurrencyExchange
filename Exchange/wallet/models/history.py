from django.db import models
from .token import Token


class History(models.Model):
    token = models.ForeignKey(Token, on_delete=models.CASCADE)
    price = models.FloatField()
    date_time = models.DateTimeField(blank=False)

    def __str__(self):
        return f"History of {self.token} - {self.date_time}"
