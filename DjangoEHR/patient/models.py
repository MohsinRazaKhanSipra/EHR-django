from django.db import models

class Receptionist(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    date_of_birth = models.DateField()
    address = models.TextField()
    hire_date = models.DateField()
    profile_picture = models.ImageField(upload_to='media/', blank=True, null=True)