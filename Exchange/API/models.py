from django.db import models


class BtcHistory(models.Model):

    price = models.FloatField()
    timestamp = models.IntegerField()

