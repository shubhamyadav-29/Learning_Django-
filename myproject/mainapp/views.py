from django.shortcuts import render

def homepage(request):
    context ={
       'page':'HomePage',
    }
    return render(request, "main.html",context )

def todolist(request):
   context = {
      'page':'TaskList'
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



