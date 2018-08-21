from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import User, UserManager
import bcrypt

# Create your views here.
def index(response):
    print(User.objects.all())
    return render(response, 'login_app/index.html')

def create_user(request):
    print('create_user view')
    print(request.POST)
    response = User.objects.validateUser(request.POST)
    if 'errors' in response:
        for error in response['errors']:
            messages.error(request, error)
        return redirect('/')
    else:
        request.session['user_id'] = response['user_id']
    return redirect('/jobs')

def login_user(request):
    response = User.objects.loginUser(request.POST)
    if 'errors' in response:
        for error in response['errors']:
            messages.error(request, error)
        return redirect('/')
    else:
        request.session['user_id'] = response['user_id']
        return redirect('/jobs')

def logout(request):
    request.session.clear()
    return redirect('/')
