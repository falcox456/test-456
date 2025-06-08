from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import login, logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Portfolio





def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
    else:
        form = RegisterForm()
    return render(request, 'app/register.html', {'form': form})



def log_in(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('profile')
    else:
        form = AuthenticationForm()
    return render(request, 'app/login.html', {'form': form})

def not_port(request):
    portfolio = Portfolio.objects.filter(is_available=True).order_by('date')
    return render(request, 'app/index.html', {'portfolio': portfolio})

@login_required
def profile(request):
   return render(request, 'app/profile.html')

@login_required
def user_logout(request):
    auth_logout(request)
    return redirect('login')

