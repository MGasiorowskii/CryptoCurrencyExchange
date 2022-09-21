from django.db import models


class BtcHistory(models.Model):

    price = models.FloatField()
    date_time = models.DateTimeField(unique=True)

