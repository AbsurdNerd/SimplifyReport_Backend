from django.urls import path, include
from .views import *

urlpatterns = [
    path('',TestAPIView.as_view()),
]