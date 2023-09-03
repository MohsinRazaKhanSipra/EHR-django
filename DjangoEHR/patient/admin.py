from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Receptionist)
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(PatientProfile)


