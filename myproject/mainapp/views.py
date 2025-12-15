from django.shortcuts import render , redirect
from mainapp.models import Task
from mainapp.forms import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

def homepage(request):
    
   return render(request, "main.html",{} )
@login_required(login_url='login')
def todolist(request):
   
   if request.method == "POST":
      form_data = TaskForm(request.POST or None)
      if form_data.is_valid():
         form_data.save()
         messages.success(request,"Task added Successfully.")
         return redirect("todolist")
      messages.success(request,"Something Went Wrong")
       
   all_tasks = Task.objects.all()
   paginator=Paginator(all_tasks, 8) 
   page = request.GET.get("page")
   
   all_tasks =paginator.get_page(page)
   
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

def delete_task(request,task_id):
   task_obj = Task.objects.get(id=task_id)
   task_obj.delete()
   messages.success(request,f"Task - {task_obj.task} deleted.")
   return redirect("todolist")

def edit_task(request,task_id):
   task_obj = Task.objects.get(id=task_id)
   if request.method == "POST":
       form_data =TaskForm(request.POST or None,instance=task_obj)
       if form_data.is_valid():
         form_data.save()
         messages.success(request,"Task Updated!")
         return redirect("todolist")
       messages.success(request,"Error Encounter in Task Updation!")
   else:
         context = {
           'task_obj': task_obj
       }
   return render(request, "edit.html",context)
   
def complete_task(request,task_id):
   task_obj = Task.objects.get(id= task_id)
   task_obj.is_completed=True
   task_obj.save()
   messages.success(request,"Status Chnaged")
   return redirect(todolist)


def pending_task(request,task_id):
   task_obj = Task.objects.get(id= task_id)
   task_obj.is_completed=False
   task_obj.save()
   messages.success(request,"Status Chnaged")
   return redirect(todolist)

   