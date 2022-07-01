from email import message
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib import messages


def register(request):

    if request.method == 'POST':
        name = request.POST['fullname']
        user_name = request.POST['user_name']
        email = request.POST['email']
        email_confirm = request.POST['email_confirm']
        password = request.POST['password']
        password_confirm = request.POST['password_confirm']


        messages.success(request, f'{name}')
        return render(request, 'appUsers/registerUser.html')

    else:

        return render(request, 'appUsers/registerUser.html')

def login(request):
    return render(request, 'appUsers/login.html')
