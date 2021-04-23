from django.shortcuts import render

from .models import Problem
from home.models import Solved
# Create your views here.


def problems(request):

    context = {}

    problems_all = Problem.objects.all()
    problem_solved = Solved.objects.all()

    context['problems'] = problems_all
    context['problem_solved'] = problem_solved

    return render(request, 'problems/problems.html', context)

def problem_by_id(request, problem_id):
    
    context = {}

    problem = Problem.objects.filter(problem_id = problem_id).first
    context['problem'] = problem

    return render(request, 'problems/problem_by_id.html', context)
