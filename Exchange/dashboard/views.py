from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from wallet.models.token import Token
from wallet.models.history import History
import plotly.graph_objs as go


EXCHANGE_PK = 13
USDT_PK = 3
TRANSACTION_FEE = 5


@login_required
def home(request):
    tokens = Token.objects.all()
    history = History.objects.filter(token_id='1').order_by('date_time')

    prices = [data.price for data in history]
    date_times = [f"{data.date_time}" for data in history]
    #trace1 = go.Scatter(x=date_times, y=prices, marker={'color': 'red', 'symbol': 104, 'size': 10},
                        #mode="lines", name='1st Trace')

    fig = go.Figure([go.Scatter(x=date_times, y=prices)])
    graph = fig.to_html(full_html=False, default_height=500, default_width=700)

    return render(request, 'dashboard/home.html', {'title': 'Dashboard',
                                                   'subtitle': 'Home',
                                                   'tokens': tokens,
                                                   'prices': prices,
                                                   'date_times': date_times,
                                                   'graph': graph})

