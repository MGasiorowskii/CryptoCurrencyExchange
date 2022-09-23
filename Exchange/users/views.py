from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin


class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'users/password_reset_form.html'
    email_template_name = 'users/password_reset_email.html'
    subject_template_name = 'users/password_reset_subject.txt'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = '/login'


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
    user_form = UserUpdateForm(instance=request.user)
    profile_form = ProfileUpdateForm(instance=request.user.profile)
    password_form = PasswordChangeForm(request.user)

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

        elif 'change_password' in request.POST:
            password_form = PasswordChangeForm(request.user, request.POST)

            if password_form.is_valid():
                password_form.save()
                update_session_auth_hash(request, password_form.user)
                messages.success(request, "Your password's been updated!")
                return redirect('profile')
            else:
                for _, error in password_form.errors.items():
                    messages.error(request, f"{error[0]}", extra_tags='danger')

    context = {'title': "Profile",
               'subtitle': 'Home',
               'user_form': user_form,
               'profile_form': profile_form,
               'password_form': password_form}

    return render(request, 'users/profile.html', context)
