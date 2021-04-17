

from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name="landing_page"),
    path('home/', views.user_home, name="home"),
    path('user/<slug:username>/', views.user_info, name="user_info")
]