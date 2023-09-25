from django.shortcuts import render, redirect
from .models import Patient
from django.http import JsonResponse, HttpResponse
from .forms import *
from django.views.generic import View
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib.auth.models import Group


def home(request):
    appointments = Appointment.objects.all()
    patient_total=Patient.objects.count()
    doctor_total=Doctor.objects.count()
    appointment_total=Appointment.objects.count()
    hospital_total=Hospital.objects.count()
    return render(request, "patient/home.html", {"appointments": appointments, "patient_total":patient_total, "doctor_total":doctor_total, "appointment_total":appointment_total, "hospital_total":hospital_total})

def login(request):
    if request.user.is_authenticated():
        return render(request, "patient/home.html")
    else:

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
            form = PatientForm()
            messages.error(request,".")
        else:
            if form.is_valid():
                form.save()
            return redirect("/patientlist")
    else:
        form = PatientForm()

    return render(request, "patient/patient.html", {"form":form})

@login_required
def patientlist(request):
    if request.method == "POST":
        form = PatientForm(request.POST)
        name = request.POST.get("name")
        email = request.POST.get("email")

        # if Patient.objects.filter(email = email, name = name).exists():
        #     print("pa")
        #     messages.error(request,".")

        # elif Patient.objects.filter(email = email).exists():
        #     messages.warning(request,".")

        if form.is_valid():
            form.save()
    else:
        form = PatientForm()
        information = Patient.objects.all()
        return render(request, "patient/patientlist.html",{"information":information, "form":form})

@login_required

def doctorinformation(request):
    if request.method == "POST":
        form = DoctorForm(request.POST)
        license_number = request.POST.get("license_number")
        if Doctor.objects.filter(license_number = license_number).exists():
            messages.error(request,"License number is already taken")

        username = request.POST.get("username")
        if Doctor.objects.filter(username = username).exists():
            messages.error(request,"username is already taken")
            
        else:
            if form.is_valid():
                form.save()
            return redirect("/doctorlist")
    else:
        form = DoctorForm()

    return render(request, "patient/doctorinformation.html", {"form":form})


@login_required
    
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

        name = request.POST.get('name')
        email = request.POST.get('email')

        if Patient.objects.filter(name = name).exists() or Patient.objects.filter(email = email).exists():
            print("PatientUpdate2")
            # messages.error(request,"Inputs already in the table")
            error_msg = "Inputs already exist"
            title = "Update Error"
            error_var = True
            information = Patient.objects.all()
            return render(request, "patient/patientlist.html",{"information":information, "error_msg":error_msg, "title":title,"error_var":error_var })
            
        else:           
            if form.is_valid():
                patient = form.save()
            
        information = Patient.objects.all()
        return render(request, "patient/patientlist.html",{"information":information})
        


class  DoctorUpdate(View):

    def  post(self, request, pk):
        data =  dict()
        doctor = Doctor.objects.get(pk=pk)
        form = DoctorForm(instance=doctor, data=request.POST)
        # name = request.POST.get('name')
        # specialization = request.POST.get('specialization')
        # contact_number = request.POST.get('contact_number')
        # license_number = request.POST.get('license_number')
        # if Doctor.objects.filter(name = name, specialization = specialization, contact_number = contact_number, license_number = license_number).exists():
        #     form = DoctorForm()
        #     messages.error(request,"Already in the Table")

        # elif Doctor.objects.filter(license_number = license_number).exists():
        #     form = DoctorForm()
        #     messages.error(request,"License number already exists")
        if form.is_valid():
            form = form.save()
            
        information = Doctor.objects.all()
        return render(request, "patient/doctorlist.html",{"information":information, "form":form})  

class  HospitalUpdate(View):

    def  post(self, request, pk):
        data =  dict()
        hospital = Hospital.objects.get(pk=pk)
        form = HospitalForm(instance=hospital, data=request.POST)
        if form.is_valid():
            form = form.save()
            
        information = Hospital.objects.all()
        return render(request, "patient/hospitallist.html",{"information":information, "form":form}) 

@login_required
def hospitalinformation(request):
    if request.method == "POST":
        form = HospitalForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/hospitallist")
    else:
        form = HospitalForm()

    return render(request, "patient/hospitalinformation.html", {"form":form})


@login_required
def hospitallist(request):
    if request.method == "POST":
        form = HospitalForm(request.POST, instance=image)
       
        if form.is_valid():
            form.save()
    else:
        form = HospitalForm()
    information = Hospital.objects.all()
    return render(request, "patient/hospitallist.html", {"information":information, "form":form})


def hospital_delete(request, pk):

    pk = pk
    try:
        image_sel = Hospital.objects.get(pk = pk)
    except Hospital.DoesNotExist:
        return redirect('hospitallist')
    image_sel.delete()
    return redirect('hospitallist')


@login_required
def appointment_list(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
        form = AppointmentForm()
        appointments = Appointment.objects.all()
        doctors = Doctor.objects.all()
        patients = Patient.objects.all()

        return render(request, 'appointments/appointment_list.html', {'appointments': appointments, "doctors":doctors,"patients" : patients, "form":form})
    else:
        form = AppointmentForm()
    appointments = Appointment.objects.all()
    doctors = Doctor.objects.all()
    patients = Patient.objects.all()

    return render(request, 'appointments/appointment_list.html', {'appointments': appointments, "doctors":doctors,"patients" : patients, "form":form})

def appointment_update(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    if request.method == 'POST':
        form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            return redirect('appointment_list')
    else:
        form = AppointmentForm(instance=appointment)
    return render(request, 'appointments/appointment_form.html', {'form': form})

def appointment_delete(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    if request.method == 'POST':
        appointment.delete()
        return redirect('appointment_list')
    return render(request, 'appointments/appointment_confirm_delete.html', {'appointment': appointment})

def doctor_appointment_view(request):
    user = request.user  # This should be a logged-in doctor user
    try:
        doctor = Doctor.objects.get(name=user)
    except Doctor.DoesNotExist:
        doctor = None  # Handle the case where there is no matching doctor
    if doctor:
        appointments = Appointment.objects.filter(doctor=doctor)
        return render(request, 'patient/doctor_appointment_view.html', {'appointments': appointments})
    else:
        appointments = Appointment.objects.all()
        return render(request, 'patient/doctor_appointment_view.html', {'appointments': appointments})
        
    

    
     #user.groups = 