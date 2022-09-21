from rest_framework.viewsets import generics
from .serializers import TokenSerializer
from .models import BtcHistory
from rest_framework.views import APIView
from rest_framework.mixins import ListModelMixin
from rest_framework.response import Response
from rest_framework import status
import requests
import datetime
import pytz


class GetAllData(generics.ListAPIView):
    serializer_class = TokenSerializer
    queryset = BtcHistory.objects.all().order_by('date_time')


class UpdateAllData(APIView, ListModelMixin):

    def get(self, request):
        for days in [365, 90, 1]:
            url = f'https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency=usd&days={days}'
            res = requests.get(url=url)
            data = res.json()

            for timestamp, price in data['prices']:

                coin_price = round(price, 2)
                timestamp = int(timestamp / 1000)
                date_time = datetime.datetime.fromtimestamp(timestamp, tz=pytz.UTC)

                if not BtcHistory.objects.filter(date_time=date_time).exists():
                    BtcHistory.objects.create(price=coin_price,
                                              date_time=date_time)

        return Response(status=status.HTTP_202_ACCEPTED)
