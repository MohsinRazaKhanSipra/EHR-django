from django.db import models
from django.contrib.auth.models import User

class Receptionist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null = True, blank = True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=False)
    phone_number = models.CharField(max_length=15)
    date_of_birth = models.DateField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    hire_date = models.DateField(blank=True, null=True)

class Doctor(models.Model):
    specialization = models.CharField(max_length=100)
    license_number = models.CharField(max_length=50)
    contact_number = models.CharField(max_length=20)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.user.username

class Patient(models.Model):
    date_of_birth = models.DateField()
    address = models.TextField()
    # contact_number = models.CharField(max_length=20)
    medical_history = models.TextField(blank=True)
    #email
    email = models.TextField(blank=True, null = True)

    def __str__(self):
        return self.user.username

    #patient prof model


class PatientProfile(models.Model):
    name =  models.OneToOneField(Patient, on_delete=models.CASCADE, null = True, blank = True)
    diagnosis = models.CharField(max_length=100, blank=True, null = True)
    drug = models.CharField(max_length=100, blank=True, null = True)
    healthCondition = models.CharField(max_length=100, blank=True, null = True)
    weight = models.IntegerField(max_length=4, blank=True, null = True)
    height = models.FloatField(blank=True, null = True)
    pregnancy = models.BooleanField(blank=True, null = True)