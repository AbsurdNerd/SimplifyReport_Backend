# Generated by Django 3.1.3 on 2020-11-12 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_ambulance_patient_problem'),
    ]

    operations = [
        migrations.AddField(
            model_name='ambulance',
            name='patient_phone_number',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]