from wallet.models.history import History
from typing import Optional
import plotly.graph_objs as go


def create_plot(token_id: int, color: Optional[str] = 'red', samples: Optional[int] = None) -> dict:
    """Returns a graph of the history of the price of a token with the given id"""

    history = History.objects.filter(token_id=token_id).order_by('-date_time')[:samples]

    prices = [data.price for data in history]
    date_times = [f"{data.date_time}" for data in history]

    fig = go.Figure([go.Scatter(x=date_times,
                                y=prices,
                                marker={'color': color, 'symbol': 100, 'size': 11},
                                mode="lines",
                                name='1st Trace')])

    graph = fig.to_html(full_html=False)

    return graph
