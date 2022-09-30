from django.db import models


class Token(models.Model):
    name = models.TextField(blank=False)
    symbol = models.TextField(max_length=10, blank=False)
    actual_price = models.FloatField(blank=False)
    image = models.ImageField(default='bitcoin_icon.jpg', upload_to='token_logo')

    def __str__(self):
        return f"{self.name}"
