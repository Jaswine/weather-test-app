from django.urls import path
from base.api.views import WeatherAPIView


urlpatterns = [
    path('weather/<str:city>/', WeatherAPIView.as_view(), name='weather'),
]