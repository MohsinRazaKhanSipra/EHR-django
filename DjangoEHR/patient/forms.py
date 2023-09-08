from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import *
from django import forms

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class PatientForm(forms.ModelForm):
    email = forms.EmailField()
    name = forms.CharField()

    class Meta:
        model = Patient
        fields = [ "name", 'email']


class DoctorForm(forms.ModelForm):
    name = forms.CharField(max_length = 100)
    specialization = forms.CharField(max_length = 100)
    license_number = forms.IntegerField()
    contact_number = forms.IntegerField()
    email = forms.EmailField()



    class Meta:
        model = Doctor
        fields = ["name", "specialization" , "license_number","contact_number", "email" ]


 


