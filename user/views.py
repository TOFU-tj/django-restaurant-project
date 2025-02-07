from django.contrib import auth
from django.urls import reverse
from django.shortcuts import render, redirect, HttpResponseRedirect
from user.models import User
from user.forms import UserLoginForm, UserRegistrationForm
from django.views.generic.edit import CreateView
from django.contrib import messages

def login(request): 
    if request.method == "POST": 
        form = UserLoginForm(data=request.POST)
        if form.is_valid(): 
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username = username, password = password)            
            if user: 
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))
    else: 
        form = UserLoginForm()
        
    context = {
        'form' : form
    }
    return render(request, 'user/login.html', context)


def logout(request): 
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))
    

def registration(request): 
    if request.method == "POST": 
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid(): 
            user = form.save()
            auth.login(request, user)
            messages.success(request, 'Поздравляем, вы успешно зарегистрировались!')
            return HttpResponseRedirect(reverse('index'))


    else: 
        form = UserRegistrationForm()
        
    context = {
        'form' : form
    }
    return render(request, 'user/register.html', context)
        
            


    
