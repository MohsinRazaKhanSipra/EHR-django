
from django.urls import path, include,re_path  
from . import views
from django.contrib.auth import views as auth_views



urlpatterns = [
    path("", views.home, name="home"),
    path("home/", views.home, name="home"),

    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path("register/", views.register, name="register"),

    path("patientinformation/", views.patientinformation, name="patientinformation"),
    path("patientlist/", views.patientlist, name="patientlist"),

    path("doctorinformation/", views.doctorinformation, name="doctorinformation"),
    path("doctorlist/", views.doctorlist, name="doctorlist"),

    path("doctorlist/delete/<int:pk>", views.doctor_delete, name="doctor_delete"),
    path("patientlist/delete/<int:pk>", views.patient_delete, name="patient_delete"),
    path("hospitallist/delete/<int:pk>", views.hospital_delete, name="hospital_delete"),


    path('patientlist/update/<int:pk>', views.PatientUpdate.as_view(), name='patientlist_update'),
    path('doctorlist/update/<int:pk>', views.DoctorUpdate.as_view(), name='doctorlist_update'),

    path("hospitalinformation/", views.hospitalinformation, name="hospitalinformation"),
    path("hospitallist/", views.hospitallist, name="hospitallist"),
    
]