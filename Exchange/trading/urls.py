from django.urls import path
from . import views

urlpatterns = [
    path("token/<slug:slug>", views.TokenDetailView.as_view(), name='token-detail'),
]
