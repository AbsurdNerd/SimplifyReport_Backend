from django.shortcuts import render
#from . import models, serializers
from rest_framework import viewsets, generics, status, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import *
import math
from fcm_django.models import FCMDevice

# Create your views here.

class UserProfileAPIView(APIView):

    def get(self, request, format=None):

        phone=request.data['phone']
        try:
            user = UserProfile.objects.get(phone=phone)
        except UserProfile.DoesNotExist:
            user = None
        if user:
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    
    def post(self, request, format=None):
        serializer = UserProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            phone=request.data['phone']
            token=request.data['token']
            FCMDevice.objects.create(device_id=phone,registration_id=token,type="android")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def put(self, request, *args, **kwargs):
        phone=request.data['phone']
        token=request.data['token']
        try:
            user = UserProfile.objects.get(phone=phone)
        except UserProfile.DoesNotExist:
            user = None
        if user:
            user.token=token
            user.save()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class FireAPIView(APIView):

    def get_queryset(self):
        fire_reports=Fire.objects.all()
        phone = self.request.query_params.get('phone')
        if phone:
            fire_reports = Fire.objects.filter(user=phone).order_by('-id')
        return fire_reports

    def get(self,request,format=None):
        queryset=self.get_queryset()
        serializer=FireSerializer(queryset,many=True)
        if serializer.data:
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

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
            for device in userstonotify:
                devices=FCMDevice.objects.filter(device_id=device)  
                devices.send_message(title="Alert ❌❌", body="Fire😱 in the range of 250m")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AmbulanceAPIView(APIView):

    def get_queryset(self):
        ambulance_reports=Ambulance.objects.all()
        phone = self.request.query_params.get('phone')
        if phone:
            ambulance_reports = Ambulance.objects.filter(user=phone).order_by('-id')
        return ambulance_reports

    def get(self,request,format=None):
        queryset=self.get_queryset()
        serializer=AmbulanceSerializer(queryset,many=True)
        if serializer.data:
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, format=None):
        serializer = AmbulanceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            reporteduser_phone= request.data['user']
            devices=FCMDevice.objects.filter(device_id=reporteduser_phone)  
            devices.send_message(title="Got your request 👍", body="Ambulance🚑 is coming soon.")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PoliceAPIView(APIView):

    def get_queryset(self):
        police_reports=Police.objects.all()
        phone = self.request.query_params.get('phone')
        if phone:
            police_reports = Police.objects.filter(user=phone).order_by('-id')
        return police_reports

    def get(self,request,format=None):
        queryset=self.get_queryset()
        serializer=PoliceSerializer(queryset,many=True)
        if serializer.data:
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

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
                for device in userstonotify:
                    devices=FCMDevice.objects.filter(device_id=device)  
                    devices.send_message(title="Alert ❌❌", body="Something is stolen🚔in the range of 250m")

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



   
        