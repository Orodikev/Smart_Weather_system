from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from .models import Preferences, WeatherData, Forecast
from .serializers import PreferencesSerializer, WeatherDataSerializer, ForecastSerializer

class PreferencesViewSet(viewsets.ModelViewSet):
    queryset = Preferences.objects.all()
    serializer_class = PreferencesSerializer

class WeatherDataViewSet(viewsets.ModelViewSet):
    queryset = WeatherData.objects.all()
    serializer_class = WeatherDataSerializer

class ForecastViewSet(viewsets.ModelViewSet):
    queryset = Forecast.objects.all()
    serializer_class = ForecastSerializer

