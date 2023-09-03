from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import *
from django import forms

class PatientForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = Patient
        fields = [ "name", 'email']


 


