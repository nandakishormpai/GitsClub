from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    return render(request, 'index.html')

def groups(request):
    return render(request, 'groups.html')

def group(request,id):
    return HttpResponse("Each group Here  " + str(id))
