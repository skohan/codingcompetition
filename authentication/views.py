import django
from django.contrib.messages.api import error
from django.forms.widgets import MediaDefiningClass
from django.shortcuts import redirect, render
from django.contrib.auth import login
from django.views import View
from django.contrib import messages

from .forms import RegistrationForm
from problems.models import Problem
from home.models import Solved

# Create your views here.


class RegistrationView(View):

    template_name   = 'authentication/register.html'
    form_class      = RegistrationForm  

    def get(self,request, *args, **kwargs):

        context = {}
        form = self.form_class()
        context['register_form'] = form

        return render(request, self.template_name, context)
    
    def post(self, request, *args, **kwargs):

        form = self.form_class(request.POST)
        print(form.data)

        if form.is_valid():
            print("------------valid--------------")
            user = form.save()
            login(request, user)

            # Setting all problems as not solved in db for user
            # all_problems = Problem.objects.all()
            # for problem in all_problems:
            #     solved = Solved(problem = problem, user = user)
            #     solved.save()

            # No need to do above code

            messages.success(request, "Successfully registered!")


            return redirect('/home')


        # messages.warning(request, "Unsuccessful registration. Invalid information.")
        # print(form.error_messages)

        for error in form.errors.as_data():
            messages.warning(request, message="{} : {}".format(error, form.errors.get(error)))
        # messages.warning(request=request, message=form.error_messages)

        print("--------------not valid--------------")

        
        context = {}
        form = self.form_class()
        context['register_form'] = form

        return render(request, self.template_name, context)


# def login(request):
#     print(request.POST)
#     return render(request, "authentication/login.html")    
# def register(request):
#     context = {}
#     form = RegistrationForm()
#     context['register_form'] = form
#     return render(request, "authentication/register.html", context=context)
