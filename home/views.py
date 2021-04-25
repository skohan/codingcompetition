from django.shortcuts import render
from django.contrib.auth.decorators import login_required


from problems.models import Problem
from home.models import Solved

from problems.utilities import get_all_problems
# Create your views here.

def landing_page(request):
    return render(request, "home/landing_page.html")

def user_info(request, username):
    return render(request, "home/user.html")

@login_required()
def user_home(request):

    context = {}

    user = request.user

    context['problems'] = get_all_problems(user)

    return render(request, "home/home.html", context)