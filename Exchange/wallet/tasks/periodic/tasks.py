import datetime
import requests
import pytz
from API.models import BtcHistory


def download_historical_data():
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


def daily_data_download():
    res = requests.get(url='https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency=usd&days=1')
    data = res.json()

    for timestamp, price in data['prices']:

        coin_price = round(price, 2)
        timestamp = int(timestamp / 1000)
        date_time = datetime.datetime.fromtimestamp(timestamp, tz=pytz.UTC)

        if not BtcHistory.objects.filter(date_time=date_time).exists():
            BtcHistory.objects.create(price=coin_price,
                                      date_time=date_time)

