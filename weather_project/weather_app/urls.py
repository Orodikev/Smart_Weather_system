from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PreferencesViewSet, WeatherDataViewSet, ForecastViewSet

router = DefaultRouter()
router.register(r'preferences', PreferencesViewSet)
router.register(r'weather', WeatherDataViewSet)
router.register(r'forecast', ForecastViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
