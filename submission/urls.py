

from django.urls import path
from .views import SubmitView

urlpatterns = [
    path('<int:problem_id>', SubmitView.as_view())
]