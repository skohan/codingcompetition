from django.shortcuts import render
from django.contrib.auth.decorators import login_required


from problems.models import Problem
from home.models import Solved
# Create your views here.

def landing_page(request):
    return render(request, "home/landing_page.html")

def user_info(request, username):
    return render(request, "home/user.html")

@login_required()
def user_home(request):

    context = {}

    user = request.user

    problems_all = Problem.objects.all()
    problem_solved = Solved.objects.filter(user=user).all()

    context['problems'] = zip(problems_all, problem_solved)

    return render(request, "home/home.html", context)