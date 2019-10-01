from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import  UserRegistrationForm, UserLoginForm

# Create your views here.


def register(request):
    if request.method == 'POST':
        form =UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('blog-home')
    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'forms': form})


def login(request):
    form = UserLoginForm(request.POST)
    return render(request, 'users/login.html', {'forms': form})
