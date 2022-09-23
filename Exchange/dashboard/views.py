from django.shortcuts import render
from wallet.models import Token


def home(request):
    tokens = Token.objects.all()
    return render(request, 'dashboard/home.html', {'title': 'Dashboard',
                                                   'subtitle': 'Home',
                                                   'tokens': tokens})
