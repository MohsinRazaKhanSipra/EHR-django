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
    class Meta:
        model = Patient
        fields = [ "name", 'email']


class DoctorForm(forms.ModelForm):
    # email = forms.EmailField()
    class Meta:
        model = Doctor
        fields = ["specialization" , "license_number","contact_number" ]


 


