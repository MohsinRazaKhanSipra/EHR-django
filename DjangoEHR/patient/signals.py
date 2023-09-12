from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import *

@receiver(post_save, sender=User)
def create_receptionist(sender, instance, created, **kwargs):
    if created:
        Receptionist.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_receptionist(sender, instance, **kwargs):
    instance.receptionist.save()

@receiver(post_save, sender=Patient)
def create_or_update_patient_profile(sender, instance, created, **kwargs):
    if created:
        PatientProfile.objects.create(patient=instance)
    else:
        instance.Doctor.save()

# @receiver(post_save, sender=Doctor)
# def create_or_update_doctor_form(sender, instance, created, **kwargs):
#     if created:
#         HospitalProfile.objects.create(patient=instance)
#     else:
#         instance.patientprofile.save()

# @receiver(post_save, sender=Doctor)
# def create_hospital_for_doctor(sender, instance, created, **kwargs):
#     if created:
#         # Create a new Hospital instance associated with the Doctor
#         Hospital.objects.create(name=f"{instance.name}'s Hospital", address=instance.address, doctor=instance)

# @receiver(post_save, sender=Doctor)
# def update_hospital_for_doctor(sender, instance, **kwargs):
#     # Update the associated Hospital instance when the Doctor is updated
#     if instance.hospital:
#         instance.hospital.name = f"{instance.name}'s Hospital"
#         instance.hospital.address = instance.address
#         instance.hospital.save()