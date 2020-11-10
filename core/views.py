from django.shortcuts import render
#from . import models, serializers
from rest_framework import viewsets, generics, status, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.


class TestAPIView(APIView):

    def get(self, request, format=None):
        return Response({'message':'Hello'},status=200)