from rest_framework import serializers
from .models import BtcHistory


class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = BtcHistory
        fields = "__all__"
