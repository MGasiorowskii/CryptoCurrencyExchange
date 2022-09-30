import datetime
import requests
import pytz
from wallet.models.token import Token
from wallet.models.history import History


TOKENS = ['bitcoin', 'ethereum', 'tether', 'binancecoin', 'solana', 'cardano']


def download_historical_data():
    for days in [365, 90, 1]:
        for token in TOKENS:
            url = f'https://api.coingecko.com/api/v3/coins/{token}/market_chart?vs_currency=usd&days={days}'
            res = requests.get(url=url)
            data = res.json()
            token_object = Token.objects.get(name=token)

            for timestamp, price in data['prices']:

                coin_price = round(price, 2)
                timestamp = int(timestamp / 1000)
                date_time = datetime.datetime.fromtimestamp(timestamp, tz=pytz.UTC)

                if not History.objects.filter(date_time=date_time, token=token_object.pk).exists():
                    History.objects.create(price=coin_price,
                                           date_time=date_time,
                                           token=token_object)


def daily_data_download():
    for token in TOKENS:
        res = requests.get(url=f'https://api.coingecko.com/api/v3/coins/{token}/market_chart?vs_currency=usd&days=1')
        data = res.json()
        token_object = Token.objects.get(name=token)

        for timestamp, price in data['prices']:

            coin_price = round(price, 2)
            timestamp = int(timestamp / 1000)
            date_time = datetime.datetime.fromtimestamp(timestamp, tz=pytz.UTC)

            if not History.objects.filter(date_time=date_time, token=token_object.pk).exists():
                History.objects.create(price=coin_price,
                                       date_time=date_time,
                                       token=token_object)

        actual_price = History.objects.filter(token=token_object.pk).values('price').latest('date_time')
        token_object.actual_price = actual_price['price']
        token_object.save()

