from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, DepositForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin
from trading.operations.get_history_transaction import get_user_history_transaction
from wallet.models.wallet import Wallet
from trading.operations.get_core_information import get_core_information
from .utils import get_user_balance


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
    profile_form = ProfileUpdateForm()
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

    user_pk = request.user.pk
    user_balance, wallet_values, wallets = get_user_balance(user_pk=user_pk)

    context = {'title': "Profile",
               'subtitle': 'Home',
               'user_form': user_form,
               'profile_form': profile_form,
               'password_form': password_form,
               'history': get_user_history_transaction(user_pk=user_pk),
               'balance': user_balance,
               'wallets': zip(wallet_values, wallets)}

    return render(request, 'users/profile.html', context)


@login_required
def deposit(request):
    form = DepositForm()

    if request.method == "POST":
        form = DepositForm(request.POST)

        if form.is_valid():
            amount = form.data['amount']
            user_pk = request.user.pk
            _, usdt_pk, _ = get_core_information()

            user_wallet = Wallet.objects.get(owner=user_pk, token=usdt_pk)
            user_wallet.quantity = float(amount) + user_wallet.quantity
            user_wallet.save()

            messages.success(request, "Your wallet has been charged!")

    return render(request, "operations/deposit.html", {"title": "Deposit",
                                                       "form": form})
