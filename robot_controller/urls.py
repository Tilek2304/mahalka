from django.urls import path
from robot_control import views

urlpatterns = [
    path('command/', views.control_command, name='control_command'),
]