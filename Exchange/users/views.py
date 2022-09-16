from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
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
    if request.method == "POST":
        if 'edit_profile' in request.POST:
            user_form = UserUpdateForm(request.POST, instance=request.user)
            profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

            if user_form.is_valid() and profile_form.is_valid():
                user_form.save()
                profile_form.save()
                messages.success(request, "Your profile's been updated!")
                return redirect('profile')
            else:
                for _, error in user_form.errors.items():
                    messages.error(request, f"{error[0]}", extra_tags='danger')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    return render(request, 'users/profile.html', {'title': "Profile", 'subtitle': 'Home', 'user_form': user_form, 'profile_form': profile_form})
