from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    is_clinic_manager = models.BooleanField(default=False)
    is_patient = models.BooleanField(default=False)


class Patient(models.Model):
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    address = models.CharField(max_length=300)
    phone_number = models.CharField(max_length=13)

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)


class Clinic(models.Model):
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    clinic_name = models.CharField(max_length=100)
    address = models.CharField(max_length=300)
    phone_number = models.CharField(max_length=13)


class Reserve(models.Model):
    clinic=models.OneToOneField(Clinic,on_delete=models.CASCADE)
    patient=models.OneToOneField(Patient,on_delete=models.CASCADE)
    reserved_time=models.DateTimeField()


