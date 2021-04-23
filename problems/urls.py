from django.urls import path

from . import views

urlpatterns = [
    path('', views.problems, name="problems"),
    path('<int:problem_id>/', views.problem_by_id, name="problem_by_id"),
]