from django.shortcuts import render,redirect
from .forms import *
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth import logout

# Create your views here.
def home(request):
    return render(request,'userProfile/home.html')
    
def register(request):
    if request.method=="POST":
        form=RegitrationForm(request.POST)
        if form.is_valid():
            var=form.save(commit=False)
            var.user=request.user
            var.save()
            return redirect ('userProfile:home')
    else:
        form=RegitrationForm()
    return render(request,'userProfile/register.html',{'form':form})

def logout_view(request):
    logout(request)
    return redirect ('userProfile:home')


