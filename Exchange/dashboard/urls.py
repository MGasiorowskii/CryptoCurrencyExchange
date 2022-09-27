from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='home-dashboard'),
    path("token/<int:pk>", views.TokenDetailView.as_view(), name='token-detail'),
]
