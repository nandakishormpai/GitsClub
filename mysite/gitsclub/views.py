from django.shortcuts import render
from django.http import HttpResponse

from .models import User

# Create your views here.

def index(request):
    return render(request, 'index.html')

def groups(request):
    users = User.objects.all()
    return render(request, 'groups.html',{'users':users})

def group(request,id):
    return HttpResponse("Each group Here  " + str(id))

# def about(request):
#     return render(request,'index.html/#about')