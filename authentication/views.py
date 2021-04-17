import django
from django.forms.widgets import MediaDefiningClass
from django.shortcuts import redirect, render
from django.contrib.auth import login
from django.views import View
from django.contrib import messages

from .forms import RegistrationForm

# Create your views here.


class RegistrationView(View):

    template_name   = 'authentication/register.html'
    form_class      = RegistrationForm  

    def get(self,request, *args, **kwargs):

        context = {}
        form = RegistrationForm()
        context['register_form'] = form

        return render(request, self.template_name, context)
    
    def post(self, request, *args, **kwargs):

        form = RegistrationForm(request.POST)
        print(form.data)

        if form.is_valid():
            print("------------valid--------------")
            user = form.save()
            login(request, user)
            username = user.username
            return redirect('/{}'.format(username))
        messages.error(request, "Unsuccessful registration. Invalid information.")
        # print(super(RegistrationView, self).errors)
        print(form.error_messages)

        messages.error(request=request, message=form.error_messages)
        print("--------------not valid--------------")

        
        context = {}
        form = RegistrationForm()
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