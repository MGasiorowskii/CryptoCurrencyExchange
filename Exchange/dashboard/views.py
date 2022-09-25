from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from wallet.models import Token


@login_required
def home(request):
    tokens = Token.objects.all()

    return render(request, 'dashboard/home.html', {'title': 'Dashboard',
                                                   'subtitle': 'Home',
                                                   'tokens': tokens})
