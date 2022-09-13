from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Dear {username}, you have been successfully signed up!")
            return redirect('login')
        else:
            for error in form.errors.values():
                messages.error(request, f"{error}", extra_tags='danger')

    else:
        form = UserRegisterForm()

    return render(request, "users/register.html", {"title": "Register", "form": form})
