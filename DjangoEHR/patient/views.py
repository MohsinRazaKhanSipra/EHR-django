from django.shortcuts import render, redirect
from .models import Patient
from django.http import JsonResponse, HttpResponse
from .forms import *
from django.views.generic import TemplateView, View, DeleteView

def home(request):
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


def patientlist(request):
    if request.method == "POST":
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = PatientForm()
    information = Patient.objects.all()
    return render(request, "patient/patientlist.html",{"information":information, "form":form})

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
    if request.method == "POST":
        form = DoctorForm(request.POST, instance=image)
        license_number = request.POST.get('license_number')
        if Doctor.objects.filter(license_number=license_number).exists():
            messages.error(response, "License Number Taken")
            return render(response, "patient/doctorinformation.html")
        if form.is_valid():
            form.save()
    else:
        form = DoctorForm()
    information = Doctor.objects.all()
    return render(request, "patient/doctorlist.html", {"information":information, "form":form})
    
    


def doctor_delete(request, pk):
    pk = pk
    try:
        image_sel = Doctor.objects.get(pk = pk)
    except Doctor.DoesNotExist:
        return redirect('doctorlist')
    image_sel.delete()
    return redirect('doctorlist')


def patient_delete(request, pk):
    pk = int(pk)
    try:
        image_sel = Patient.objects.get(pk = pk)
    except Patient.DoesNotExist:
        return redirect('patientlist')
    image_sel.delete()
    return redirect('patientlist')

class  PatientUpdate(View):
    def  post(self, request, pk):
        data =  dict()
        patient = Patient.objects.get(pk=pk)
        form = PatientForm(instance=patient, data=request.POST)
        if form.is_valid():
            patient = form.save()
            
        information = Patient.objects.all()
        return render(request, "patient/patientlist.html",{"information":information, "form":form})
        

class  DoctorUpdate(View):
    def  post(self, request, pk):
        data =  dict()
        doctor = Doctor.objects.get(pk=pk)
        form = DoctorForm(instance=doctor, data=request.POST)
        if form.is_valid():
            doctor = form.save()
            
        information = Doctor.objects.all()
        return render(request, "patient/doctorlist.html",{"information":information, "form":form})  