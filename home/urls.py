

from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page),
    path('<slug:username>/', views.user_info)
]