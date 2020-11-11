from django.urls import path, include
from .views import *

urlpatterns = [
    path('profile/',UserProfileAPIView.as_view()),
    path('fire/',FireAPIView.as_view()),
    path('ambulance/',AmbulanceAPIView.as_view()),
    path('police/',PoliceAPIView.as_view()),
]