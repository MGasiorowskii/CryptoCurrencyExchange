import django.template.backends.django
from rest_framework.viewsets import generics
from .serializers import TokenSerializer
from .models import BtcHistory


class UpdateAllData(generics.ListAPIView):
    serializer_class = TokenSerializer
    queryset = BtcHistory.objects.all()

