from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm, DateInput
from django.utils import timezone
from .models import *
from django import forms

class DateInput(forms.DateInput):
    input_type = 'date'

class RegisterForm(UserCreationForm):
    username = forms.CharField()
    name = forms.CharField()
    
    class Meta:
        model = User
        fields = ["username", "name","password1", "password2"]

class PatientForm(forms.ModelForm):
    email = forms.EmailField()
    name = forms.CharField()
    
    class Meta:
        model = Patient
        fields = [ "name", 'email',"date_of_birth"]
        widgets = {
            'date_of_birth': DateInput(),
        }



class DoctorForm(forms.ModelForm):

    class Meta:
        model = Doctor
        fields = [ "username", "password", "name", "specialization" , "license_number","contact_number" ]
    widgets = {
                'date_of_birth': DateInput(),
            }
class HospitalForm(forms.ModelForm):
    name = forms.CharField()
    address = forms.CharField()
    

    class Meta:
        model = Hospital
        fields = ["name", "address"]


    def clean(self):
        #patientS
        #event title, event detail
        cleaned_data = super().clean()
        start_datetime = cleaned_data.get('start_datetime')
        end_datetime = cleaned_data.get('end_datetime')
        doctor = cleaned_data.get('doctor')
        hospital = cleaned_data.get('hospital')

        # Check if any of the required fields are None
        if start_datetime is None or end_datetime is None or doctor is None or hospital is None:
            raise ValidationError('One or more required fields are missing.')

        # Check for overlapping appointments
        overlapping_appointments = Appointment.objects.filter(
            doctor=doctor,
            hospital=hospital,
            start_datetime__lt=end_datetime,
            end_datetime__gt=start_datetime,
        )
        
        if self.instance:
            overlapping_appointments = overlapping_appointments.exclude(pk=self.instance.pk)

        if overlapping_appointments.exists():
            raise ValidationError('This appointment overlaps with an existing appointment.')

        return cleaned_data


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ["title", "start_datetime", "end_datetime", "hospital", "patient", "doctor"]
        widgets = {
            'start_datetime': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'end_datetime': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Set initial values for start_datetime and end_datetime fields
        current_datetime = timezone.localtime()
        formatted_date = current_datetime.strftime('%Y-%m-%dT%H:%M')
        self.initial['start_datetime'] = formatted_date
        

    def clean(self):
        #patientS
        #event title, event detail
        cleaned_data = super().clean()
        start_datetime = cleaned_data.get('start_datetime')
        end_datetime = cleaned_data.get('end_datetime')
        doctor = cleaned_data.get('doctor')
        hospital = cleaned_data.get('hospital')

        # Check if any of the required fields are None
        if start_datetime is None or end_datetime is None or doctor is None or hospital is None:
            raise ValidationError('One or more required fields are missing.')

        # Check for overlapping appointments
        overlapping_appointments = Appointment.objects.filter(
            doctor=doctor,
            hospital=hospital,
            start_datetime__lt=end_datetime,
            end_datetime__gt=start_datetime,
        )
        
        if self.instance:
            overlapping_appointments = overlapping_appointments.exclude(pk=self.instance.pk)

        if overlapping_appointments.exists():
            raise ValidationError('This appointment overlaps with an existing appointment.')