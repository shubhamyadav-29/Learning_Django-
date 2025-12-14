from django.shortcuts import render,redirect
from .forms import CustomRegistrationForm
from django.contrib import messages
# Create your views here.

def register(request):
    if request.method == "POST":
        register_form = CustomRegistrationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, "User Created successfully")
            return redirect("todolist")
    else:
        register_form = CustomRegistrationForm()
    return render(request,'register.html',{'register_form':register_form})
    

from django.http import HttpResponse

def debug_logout(request):
    return HttpResponse(f"METHOD = {request.method}")

