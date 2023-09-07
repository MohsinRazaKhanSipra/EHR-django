
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

    path("doctorlist/delete/<int:image_id>", views.doctor_delete, name="doctor_delete"),
    path("patientlist/delete/<int:image_id>", views.patientlist, name="patientlist"),

    path('patientlist/update/<int:pk>', views.RoomUpdate.as_view(), name='patientlist_update'),
    # path("doctorlist/update/<int:image_id>", views.doctor_update, name="doctor_update"),

    # URL pattern for getting patient data for the modal
    # path('get_patient/<int:patient_id>/', views.get_patient, name='get_patient'),

    # # URL pattern for updating patient data via AJAX
    # path('update_patient/<int:patient_id>/', views.update_patient, name='update_patient'),
]