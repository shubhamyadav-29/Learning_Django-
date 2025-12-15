from django.shortcuts import render,redirect
from .forms import CustomRegistrationForm
from django.contrib import messages
from django.contrib.auth import logout

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
    
def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("login")   # or redirect to logout page URL

    return redirect("login")