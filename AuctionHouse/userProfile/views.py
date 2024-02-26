from django.shortcuts import render,redirect,get_object_or_404
from .forms import *
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth import logout


# Create your views here.
def home(request):
    return render(request,'userProfile/home.html')

def aboutUs(request):
    return render(request,'userProfile/aboutUs.html')  

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

def profile_view(request):
    profile = get_object_or_404(Buyer_Seller, user=request.user)
    return render(request,'userProfile/profile_view.html',{'profile':profile})

