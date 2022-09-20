from django.urls import path
from .views import UpdateAllData

urlpatterns = [
    path('update-db/', UpdateAllData.as_view(), name='update_crypto_data'),
]
