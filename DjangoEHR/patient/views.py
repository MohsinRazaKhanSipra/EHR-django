from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Patient

from django.contrib.auth.decorators import login_required
from .forms import *

# Create your views here.
def home(request):
    # if request.user.is_authenticated:
    #     image = UserProfile.objects.filter(user=request.user).first().profile_picture
    #     if image:
    #         request.session["image"] = image.url

    return render(request, "patient/home.html")

def login(request):
    return render(request, "registration/login.html")


def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
        return redirect("/home")
    else:
        form = RegisterForm()

        return render(response, "patient/register.html", {"form":form})



def patientinformation(response):
    if response.method == "POST":
        form = PatientForm(response.POST)
        if form.is_valid():
            form.save()
        return redirect("/patientlist")
    else:
        form = PatientForm()

        return render(response, "patient/patient.html", {"form":form})


# @login_required
def patientlist(request):
    
    # info = Patient.objects.filter(user=request.user)

    information = Patient.objects.all()
    return render(request, "patient/patientlist.html",{"information":information})

def doctorinformation(response):
    if response.method == "POST":
        form = DoctorForm(response.POST)
        if form.is_valid():
            form.save()
        return redirect("/doctorlist")
    else:
        form = DoctorForm()

        return render(response, "patient/doctorinformation.html", {"form":form})


    
def doctorlist(request):
    
    

    information = Doctor.objects.all()
    return render(request, "patient/doctorlist.html", {"information":information})

def doctor_update(request, image_id):
    image = Doctor.objects.get(pk=image_id)
    if request.method == "POST":
        form = DoctorForm(request.POST, request.FILES, instance=image)
        if form.is_valid():
            form.save()
            return redirect('doctorlist')  # Redirect to myrecord page after successful update
    else:
        form = DoctorForm(instance=image)
    return render(request, "patient/doctorlist.html", {"form": form})


def doctor_delete(request, image_id):
    img_id = int(image_id)
    try:
        image_sel = Doctor.objects.get(id = img_id)
    except Doctor.DoesNotExist:
        return redirect('doctorlist')
    image_sel.delete()
    return redirect('doctorlist')

def patient_update(request, image_id):
    image = Patient.objects.get(pk=image_id)
    if request.method == "POST":
        form = DoctorForm(request.POST, request.FILES, instance=image)
        if form.is_valid():
            form.save()
            return redirect('patientlist')  # Redirect to myrecord page after successful update
    else:
        form = DoctorForm(instance=image)
    return render(request, "patient/patientlist.html", {"form": form})


def patient_delete(request, image_id):
    img_id = int(image_id)
    try:
        image_sel = Patient.objects.get(id = img_id)
    except Patient.DoesNotExist:
        return redirect('patientlist')
    image_sel.delete()
    return redirect('patientlist')





