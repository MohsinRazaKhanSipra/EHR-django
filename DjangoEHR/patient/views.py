from django.shortcuts import render
from django.shortcuts import render, redirect


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