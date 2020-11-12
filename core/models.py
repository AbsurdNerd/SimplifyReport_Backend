from django.db import models
from django.core.validators import RegexValidator
# Create your models here.

gender_choices= (
    ("Male","Male"),
    ("Female","Female"),
    ("Other","Other"),
)

blood_group_choices = (
    ("A+","A+"),
    ("O+","O+"),
    ("B+","B+"),
    ("AB+","AB+"),
    ("A-","A-"),
    ("O-","O-"),
    ("B-","B-"),
    ("AB-","AB-"),
)


class UserProfile(models.Model):

    name=models.CharField(max_length=100)
    phone=models.CharField(max_length=15, unique=True)
    gender=models.CharField(max_length=10,choices=gender_choices)
    location=models.CharField(max_length=100)
    permanent_address=models.TextField(max_length=500)
    token=models.TextField(max_length=512,blank=True, null=True)

    def __str__(self):
        return self.name




class Fire(models.Model):

    user=models.ForeignKey(UserProfile,on_delete=models.CASCADE, to_field='phone')
    location=models.CharField(max_length=100)
    address=models.TextField(max_length=500)
    created=models.DateTimeField(auto_now_add=True,blank=True,null=True)

    def __str__(self):
        return self.user.name


class Ambulance(models.Model):

    user=models.ForeignKey(UserProfile,on_delete=models.CASCADE, to_field='phone')
    patient_name=models.CharField(max_length=100,null=True,blank=True)
    patient_phone_number=models.CharField(max_length=15,null=True,blank=True)
    location=models.CharField(max_length=100)
    address=models.TextField(max_length=500)
    age=models.IntegerField()
    gender=models.CharField(max_length=10,choices=gender_choices)
    blood_group=models.CharField(max_length=5,choices=blood_group_choices)
    patient_problem=models.TextField(max_length=500,blank=True,null=True)
    created=models.DateTimeField(auto_now_add=True,blank=True,null=True)

    def __str__(self):
        return self.user.name


class Police(models.Model):

    user=models.ForeignKey(UserProfile,on_delete=models.CASCADE, to_field='phone')
    location=models.CharField(max_length=100)
    address=models.TextField(max_length=500)
    problem=models.CharField(max_length=100)
    problem_description=models.TextField(max_length=500)
    image=models.ImageField(upload_to="policereport/",blank=True,null=True)
    do_notify=models.BooleanField(default=False)
    created=models.DateTimeField(auto_now_add=True,blank=True,null=True)

    def __str__(self):
        return self.user.name