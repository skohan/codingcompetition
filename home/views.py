from django.shortcuts import render

# Create your views here.

def landing_page(request):
    return render(request, "home/landing_page.html")

def user_info(request, username):
    return render(request, "home/user.html")