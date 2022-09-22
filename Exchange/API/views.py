from rest_framework.viewsets import generics
from .serializers import TokenSerializer
from .models import BtcHistory
from rest_framework.views import APIView
from rest_framework.mixins import ListModelMixin
from rest_framework.response import Response
from rest_framework import status
import requests
import datetime
import pytz


class GetAllData(generics.ListAPIView):
    serializer_class = TokenSerializer
    queryset = BtcHistory.objects.all().order_by('date_time')
