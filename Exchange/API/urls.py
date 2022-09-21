from django.urls import path
from .views import GetAllData, UpdateAllData

urlpatterns = [
    path('get-db/', GetAllData.as_view(), name='get_crypto_data'),
    path('update-db/', UpdateAllData.as_view(), name='update_crypto_data'),
]
