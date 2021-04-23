
from django.contrib.auth import views as auth_view
from django.urls import path
from . import views

urlpatterns = [
    path('login/',       auth_view.LoginView.as_view(template_name="authentication/login.html"), name="login"),
    path('logout/',      auth_view.LogoutView.as_view(template_name = "home/landing_page.html"), name="logout"),
    path('register/',    views.RegistrationView.as_view(), name="register"),
]