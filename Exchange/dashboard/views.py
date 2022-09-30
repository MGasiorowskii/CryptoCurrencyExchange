from django.shortcuts import render
from wallet.models.token import Token
from .utils import create_plot


def home(request):
    tokens = Token.objects.all()

    graph = create_plot(token_id=1)

    return render(request, 'dashboard/home.html', {'title': 'Dashboard',
                                                   'subtitle': 'Home',
                                                   'tokens': tokens,
                                                   'graph': graph})

