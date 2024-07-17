from django.urls import path
from base.api.views import WeatherAPIView, CityListAPIView


urlpatterns = [
    path('weather/<str:city>/', WeatherAPIView.as_view(), name='weather'),
    path('cities/', CityListAPIView.as_view(), name='cities'),
]