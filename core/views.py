from django.shortcuts import render
#from . import models, serializers
from rest_framework import viewsets, generics, status, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import *
# Create your views here.


class UserProfileAPIView(generics.ListCreateAPIView):

    queryset=UserProfile.objects.all()
    serializer_class=UserProfileSerializer


class FireAPIView(generics.ListCreateAPIView):

    queryset=Fire.objects.all()
    serializer_class=FireSerializer


class AmbulanceAPIView(generics.ListCreateAPIView):

    queryset=Ambulance.objects.all()
    serializer_class=AmbulanceSerializer


class PoliceAPIView(generics.ListCreateAPIView):

    queryset=Police.objects.all()
    serializer_class=PoliceSerializer
