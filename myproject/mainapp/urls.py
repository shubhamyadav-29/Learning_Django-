from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('todolist', views.todolist, name='home'),
    path('contact', views.contact, name='home'),
    path('about', views.about, name='home'),
]
