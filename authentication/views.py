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

            messages.success(request, "Successfully registered!")

            return redirect('/home')



        print("--------------not valid--------------")

        
        context = {}
        context['register_form'] = form

        return render(request, self.template_name, context)

