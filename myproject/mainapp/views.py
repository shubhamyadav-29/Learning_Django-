from django.shortcuts import render

from django.http import HttpResponse,JsonResponse

def home(request):
    data = {
        "name":"Shubham",
        "location":"mumbai"
    }
    return JsonResponse(data)



# Create your views here.
