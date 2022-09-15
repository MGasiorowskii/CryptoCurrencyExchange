from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def register(request):

    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Dear {username}, you have been successfully signed up!")
            return redirect('login')

    else:
        form = UserRegisterForm()

    return render(request, "users/register.html", {"title": "Register", "form": form})


@login_required
def profile(request):
    return render(request, 'users/profile.html', {'title': "Profile", 'subtitle': 'Home'})
