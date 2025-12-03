from django.urls import path
from . import views

urlpatterns = [
    path('todolist', views.home, name='home'),
]
