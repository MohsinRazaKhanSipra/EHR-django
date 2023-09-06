from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .models import Patient
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .forms import *
from django.views.decorators.csrf import csrf_exempt
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
        if form.is_valid():
            form.save()
    else:
        form = DoctorForm()
    information = Doctor.objects.all()
    return render(request, "patient/doctorlist.html", {"information":information})
    
    


def doctor_update(request, image_id):
    image = Doctor.objects.get(pk=image_id)
    if request.method == "POST":
        form = DoctorForm(request.POST, instance=image)
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

# def patient_update(request, patient_id):
#     patient = get_object_or_404(Patient, pk=patient_id)

#     if request.method == "POST":
#         form = PatientForm(request.POST, request.FILES, instance=patient)
#         if form.is_valid():
#             form.save()
#             return redirect('patientlist')  # Redirect to the patient list page after a successful update
#     else:
#         form = PatientForm(instance=patient)

#     return render(request, "patient/patient_update.html", {"form": form, "patient": patient})


def patient_delete(request, image_id):
    img_id = int(image_id)
    try:
        image_sel = Patient.objects.get(id = img_id)
    except Patient.DoesNotExist:
        return redirect('patientlist')
    image_sel.delete()
    return redirect('patientlist')


@csrf_exempt
def get_patient(request, patient_id):
    patient = Patient.objects.get(pk=patient_id)
    data = {
        'name': patient.name,
        'specialization': patient.specialization,
        'license_number': patient.license_number,
        'contact_number': patient.contact_number,
    }
    return JsonResponse(data)


@csrf_exempt
def update_patient(request, patient_id):
    patient = Patient.objects.get(pk=patient_id)

    if request.method == "POST":
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            return JsonResponse({'status': 'success'})

    return JsonResponse({'status': 'error'})

