
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# Form for registration


class RegistrationForm(UserCreationForm):

    email = forms.EmailField(required=True, help_text = "Write your email address")

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
    
    def save(self,  commit = True):
        user = super(RegistrationForm, self).save(commit=False)
        email = self.cleaned_data['email']
        user.email = email

        if commit:
            user.save()
        
        return user