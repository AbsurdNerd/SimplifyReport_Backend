from rest_framework import serializers
from .models import *



class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = '__all__'


class FireSerializer(serializers.ModelSerializer):

    class Meta:
        model = Fire
        fields = '__all__'


class AmbulanceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ambulance
        fields = '__all__'


class PoliceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Police
        fields = '__all__'



