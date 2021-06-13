from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Problem
from home.models import Solved
from problems.utilities import get_all_problems
# Create your views here.


@login_required()
def problems(request):

    context = {}

    user = request.user

    context['problems'] = get_all_problems(user)

    return render(request, 'home/home.html', context)

    
@login_required()
def problem_by_id(request, problem_id):
    
    context = {}

    problem = Problem.objects.filter(problem_id = problem_id).first
    context['problem'] = problem

    return render(request, 'problems/problem_by_id.html', context)
