from django.shortcuts import render

def homepage(request):
   return render(request, "main.html" )

def todolist(request):
   return render(request, "todolist.html" )

def contact(request):
   return render(request, "contact.html" )

def about(request):
   return render(request, "about.html" )



