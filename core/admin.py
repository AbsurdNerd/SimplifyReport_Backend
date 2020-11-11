from django.contrib import admin
from .models import UserProfile, Fire, Ambulance, Police
# Register your models here.


admin.site.register(UserProfile)
admin.site.register(Fire)
admin.site.register(Ambulance)
admin.site.register(Police)