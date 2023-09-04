
from django.urls import path, include
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

    path("doctorlist/delete/<int:image_id>", views.doctor_delete, name="doctor_delete"),
    path("doctorlist/update/<int:image_id>", views.doctor_update, name="doctor_update"),

    path("patientlist/delete/<int:image_id>", views.patient_delete, name="doctor_delete"),
    path("patientlist/update/<int:image_id>", views.patient_update, name="doctor_update"),
]

