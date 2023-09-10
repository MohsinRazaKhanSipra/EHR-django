from django.shortcuts import render, redirect
from .models import Patient
from django.http import JsonResponse, HttpResponse
from .forms import *
from django.views.generic import TemplateView, View, DeleteView
from django.contrib import messages



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



def patientinformation(request):
    if request.method == "POST":
        form = PatientForm(request.POST)
        email = request.POST.get("email")
        if Patient.objects.filter(email = email).exists():
            messages.error(request,"Email already taken")
        if form.is_valid():
            form.save()
        return redirect("/patientlist")
    else:
        form = PatientForm()

        return render(request, "patient/patient.html", {"form":form})


def patientlist(request):
    if request.method == "POST":
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = PatientForm()
    information = Patient.objects.all()
    return render(request, "patient/patientlist.html",{"information":information, "form":form})

def doctorinformation(request):
    if request.method == "POST":
        form = DoctorForm(request.POST)
        license_number = request.POST.get("license_number")
        if Doctor.objects.filter(license_number = license_number).exists():
            messages.error(request,"License number is already taken")
            
        else:
            if form.is_valid():
                form.save()
            return redirect("/doctorlist")
    else:
        form = DoctorForm()

    return render(request, "patient/doctorinformation.html", {"form":form})


    
def doctorlist(request):
    if request.method == "POST":
        form = DoctorForm(request.POST, instance=image)
        # name = request.POST.get('name')
        # specialization = request.POST.get('specialization')
        # contact_number = request.POST.get('contact_number')
        # license_number = request.POST.get('license_number')
        # if Doctor.objects.filter(name = name, specialization = specialization, contact_number = contact_number, license_number = license_number).exists():
        #     messages.error(request,"Fields already in the Table")
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
    pk = pk
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
        name = request.POST.get('name')
        specialization = request.POST.get('specialization')
        contact_number = request.POST.get('contact_number')
        license_number = request.POST.get('license_number')
        if Doctor.objects.filter(name = name, specialization = specialization, contact_number = contact_number, license_number = license_number).exists():
            print("debug 1")
            messages.error(request,"Already in the Table")
        elif Doctor.objects.filter(license_number = license_number).exists():
            print("debug 2")
            messages.error(request,"License number already exists")
        else:
            form = DoctorForm(instance=doctor, data=request.POST)
            if form.is_valid():
                doctor = form.save()
        form = DoctorForm()    
        information = Doctor.objects.all()
        return render(request, "patient/doctorlist.html",{"information":information, "form":form})  