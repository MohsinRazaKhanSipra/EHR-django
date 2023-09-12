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
    name = forms.CharField()
    specialization = forms.CharField()
    license_number = forms.IntegerField()
    contact_number = forms.IntegerField()

    class Meta:
        model = Doctor
        fields = ["name", "specialization" , "license_number","contact_number" ]

class HospitalForm(forms.ModelForm):
    name = forms.CharField()
    address = forms.CharField()
    

    class Meta:
        model = Hospital
        fields = ["name", "address"]