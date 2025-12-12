from django.shortcuts import render , redirect
from mainapp.models import Task
from mainapp.forms import TaskForm

def homepage(request):
    context ={
       'page':'HomePage',
    }
    return render(request, "main.html",context )

def todolist(request):
   
   if request.method == "POST":
      form_data = TaskForm(request.POST or None)
      if form_data.is_valid():
         form_data.save()
         return redirect("todolist")
      
   all_tasks = Task.objects.all()
   context = {
      'page':'TaskList',
      'all_tasks':all_tasks,
   }
   return render(request, "todolist.html",context )

def contact(request):
   context={
      'page':'Contact'
   }
   return render(request, "contact.html",context )

def about(request):
   context = {
      'page':'About'
   }
   return render(request, "about.html",context )



