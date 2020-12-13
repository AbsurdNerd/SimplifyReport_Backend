from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Ambulance, Fire, Police
from django.core.mail import send_mail
from django.conf import settings 

@receiver(post_save, sender=Fire)
def fire_alert(sender, instance=None, **kwargs):
    """
    A mail whenever a new fire incident is noticed and registered into the system.
    """
    if kwargs['created']:
        subject='Fire incident!' #Subject of the mail
        recipient_list = [] #User email list to be mailed
        sender_mail = settings.EMAIL_HOST_USER # Sender Email  
        content= "A fire incident has taken place in your locality! Please take care." # Body of the message
        send_mail(
            subject= subject, 
            message=content, 
            from_email= sender_mail, 
            recipient_list=recipient_list, 
            fail_silently=False
        )
    else:
        pass