from django.db import models
from django.contrib.auth.models import User

class Preferences(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email_notifications = models.BooleanField(default=True)
    sms_notifications = models.BooleanField(default=False)
    push_notifications = models.BooleanField(default=False)
    alert_types = models.JSONField(default=list)

class WeatherData(models.Model):
    location = models.CharField(max_length=255)
    temperature = models.DecimalField(max_digits=5, decimal_places=2)
    humidity = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

class Forecast(models.Model):
    location = models.CharField(max_length=255)
    date = models.DateField()
    temperature = models.DecimalField(max_digits=5, decimal_places=2)
    humidity = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.CharField(max_length=255)
