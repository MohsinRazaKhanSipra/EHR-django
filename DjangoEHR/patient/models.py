from django.contrib.auth.models import User, Group
import random
import string
from django.db import models
from datetime import datetime
from django.urls import reverse
from django.contrib.auth.models import AbstractUser



class Hospital(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    address = models.TextField()
    def __str__(self):
        return self.name

class Receptionist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=False)
    phone_number = models.CharField(max_length=15)
    date_of_birth = models.DateField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)


class Doctor(models.Model):
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255, default = "123")
    # user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    gender = models.CharField(max_length=100, null=True, blank=True)
    specialization = models.CharField(max_length=100, null=True, blank=True)
    license_number = models.CharField(max_length=50, null=True, blank=True)
    contact_number = models.CharField(max_length=20, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    hospital = models.OneToOneField(Hospital, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

class Patient(models.Model):
    
    id = models.AutoField(primary_key=True) 
    name = models.CharField(max_length=25, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    address = models.TextField()
    medical_history = models.TextField(blank=True)
    email = models.EmailField(blank=True, null=True)
    MRN = models.CharField(max_length=20, unique=True, null=True)

    def __str__(self):
        return str(self.name)


    def save(self, *args, **kwargs):
        if not self.MRN:
            self.MRN = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(20))
        super().save(*args, **kwargs)

class PatientProfile(models.Model):
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE, null=True, blank=True)
    diagnosis = models.CharField(max_length=100, blank=True, null=True)
    drug = models.CharField(max_length=100, blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)
    height = models.FloatField(blank=True, null=True)
    pregnancy = models.BooleanField(blank=True, null=True)
    
    def __str__(self):
        return str(self.id)

class Appointment(models.Model):
    id = models.AutoField(primary_key=True) 

    title = models.CharField(max_length=100)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    detail = models.TextField()
    hospital = models.ForeignKey('Hospital', on_delete=models.CASCADE)
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE)
    doctor = models.ForeignKey('Doctor', on_delete=models.CASCADE)

    def __str__(self):
        return self.title



