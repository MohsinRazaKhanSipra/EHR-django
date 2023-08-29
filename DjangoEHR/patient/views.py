from django.shortcuts import render

# Create your views here.
def home(request):
    # if request.user.is_authenticated:
    #     image = UserProfile.objects.filter(user=request.user).first().profile_picture
    #     if image:
    #         request.session["image"] = image.url

    return render(request, "patient/home.html")