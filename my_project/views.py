from email import message
from django.shortcuts import render
from django.http import HttpResponse
from my_project.models import Task
from django.contrib import messages
from django.contrib.auth.models import User
from .models import *

# Create your views here.
def start(request):
    return render(request, 'login.html')

def register(request):
    if request.method=='POST':
        username=request.POST.get['username']
        password=request.POST.get['pass']
        re_password=request.POST.get['re_pass']
        newuser=User.objects.create_user(username,password,re_password)
        newuser.save()
        message.success(request,"YOU ALREADY HAVE AN ACCOUNT!!")
    
    return render(request, 'register.html')

def task(request):
    if request.method == 'POST':
        if request.POST.get('title') and request.POST.get('description'):
            post=Task()
            post.title= request.POST.get('title')
            post.description= request.POST.get('description')
            post.complete= request.POST.get('complete')
            post.save()
            return render(request, 'task.html')  

    else:
        return render(request,'task.html')