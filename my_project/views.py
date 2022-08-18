from multiprocessing import AuthenticationError
import re
from django.shortcuts import render
from django.http import HttpResponse
from my_project.models import Task
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import *

# Create your views here.


def start(request):
    # if request.method == 'POST':
    #     form = AuthenticationForm()
    # else:
    #     form = AuthenticationForm()

    # return render(request, 'login.html', {'form': form})
    queryset = User.objects.all('username')
    for user in queryset:
        if user:
            return render(request, 'welcome.html')
        else:
            return render(request, 'login.html')

    session = Session.objects.get(session_key='session_key')
    session_data = session.get_decoded()
    print(session_data)
    uid = session_data.get('_auth_user_id')
    user = User.objects.get(id=uid)
    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        if request.POST.get('uname') and request.POST.get('psw'):
            username = request.POST.get('uname')
            password = request.POST["psw"]
            confirmation = request.POST["psw-repeat"]
            if password != confirmation:
                return render(request, "register.html", {
                    "message": "Passwords must match."})
            else:
                newuser = User.objects.create_user(username, password)
                newuser.save()
                messages.success(request, "YOU ALREADY HAVE AN ACCOUNT!!")
                return render(request, 'welcome.html')
    return render(request, 'register.html')


def task(request):
    if request.method == 'POST':
        if request.POST.get('title') and request.POST.get('description'):
            post = Task()
            post.title = request.POST.get('title')
            post.description = request.POST.get('description')
            post.complete = True
            post.save()
            return render(request, 'welcome.html', post)

    else:
        return render(request, 'task.html')


def welcome(request):
    # user=User.objects.get('username')
    session = Session.objects.get(session_key='session_key')
    session_data = session.get_decoded()
    print(session_data)
    uid = session_data.get('_auth_user_id')
    user = User.objects.get(id=uid)
    return render(request, 'welcome.html', user)
