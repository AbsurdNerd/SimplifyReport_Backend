from django.shortcuts import render
#from . import models, serializers
from rest_framework import viewsets, generics, status, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import *
import math

# Create your views here.


class UserProfileAPIView(generics.ListCreateAPIView):

    queryset=UserProfile.objects.all()
    serializer_class=UserProfileSerializer


class FireAPIView(APIView):

    def get(self, request, format=None):
        fire_reports = Fire.objects.all()
        serializer = FireSerializer(fire_reports, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = FireSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            loc1=request.data['location']
            reporteduser_phone= request.data['user']
            res = [j.strip() for j in loc1.split(',')]
            lat1=float(res[0])
            lon1=float(res[1])

            userstonotify=[]
            for i in UserProfile.objects.all():
                loc2=i.location
                #print(loc2)
                res = [j.strip() for j in loc2.split(',')]
                lat2=float(res[0])
                lon2=float(res[1])
                radius = 6371 
                dlat = math.radians(lat2-lat1)
                dlon = math.radians(lon2-lon1)
                a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon/2) * math.sin(dlon/2)
                c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
                d = radius*c*1000  #gives distance in metres
                if d<=250 and i.phone!=reporteduser_phone:
                    userstonotify.append(i.phone)
                #print(userstonotify)
            return Response(userstonotify, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AmbulanceAPIView(APIView):

    def get(self, request, format=None):
        ambulance_reports = Ambulance.objects.all()
        serializer = AmbulanceSerializer(ambulance_reports, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AmbulanceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PoliceAPIView(APIView):

    def get(self, request, format=None):
        police_reports = Police.objects.all()
        serializer = PoliceSerializer(police_reports, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PoliceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            do_notify = request.data['do_notify']
            reporteduser_phone= request.data['user']
            if do_notify:
                loc1=request.data['location']
                res = [j.strip() for j in loc1.split(',')]
                lat1=float(res[0])
                lon1=float(res[1])

                userstonotify=[]
                for i in UserProfile.objects.all():
                    loc2=i.location
                    #print(loc2)
                    res = [j.strip() for j in loc2.split(',')]
                    lat2=float(res[0])
                    lon2=float(res[1])
                    radius = 6371 
                    dlat = math.radians(lat2-lat1)
                    dlon = math.radians(lon2-lon1)
                    a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon/2) * math.sin(dlon/2)
                    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
                    d = radius*c*1000  #gives distance in metres
                    if d<=250 and i.phone!=reporteduser_phone:
                        userstonotify.append(i.phone)
                #print(userstonotify)

            return Response(userstonotify, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)