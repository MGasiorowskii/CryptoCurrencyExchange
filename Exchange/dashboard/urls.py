from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='home-dashboard'),
    path("token/<slug:slug>", views.TokenDetailView.as_view(), name='token-detail'),
]
