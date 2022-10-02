from django.urls import path
from django.contrib.auth import views as auth_views
from users import views as user_views
from django.conf import settings
from users.views import ResetPasswordView
from django.conf.urls.static import static


urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html', extra_context={'title': 'Login'}), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html', extra_context={'title': 'Logout'}), name='logout'),
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('profile/deposit/', user_views.deposit, name='deposit'),
    path("password-reset/", ResetPasswordView.as_view(), name='password-reset'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
         name='password_reset_complete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
