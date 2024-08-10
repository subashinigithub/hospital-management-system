from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.conf import settings
from .forms import *

from django.contrib.auth.models import User


def index(r):
    return render(r,'index.html')


def register(r):
    if r.user.is_authenticated and r.user.is_staff:
        if r.method=='POST':
            form=hospitalform(r.POST,r.FILES)
            if form.is_valid():
                form.save()
            return redirect('admindb')
        else:
            form=hospitalform()
        return render(r,'adminview/adminreg.html',{'form':form})
    else:
        return redirect('adminlog')
    
def admindashboard(r):
    if r.user.is_authenticated and r.user.is_staff:
        return render(r,'adminview/admindashboard.html')
    else:
        return redirect('adminlog')
        
def adminlogin(r):
    if r.user.is_authenticated and r.user.is_staff:
        return redirect('admindb')
    message=""
    if r.method =='POST':
        username=r.POST.get('username')
        password=r.POST.get('password')
        print(username,password)
        user=authenticate(r,username=username, password=password)
        if user is not None and user.is_staff:
            login(r,user)
            return redirect('admindb')
        else:
            message="Invalid Username or Password"

    return render(r,'adminview/admin.html',{'message':message})

@login_required(login_url='/adminlogin/')
def adminlogout(r):
    logout(r)
    return redirect('adminlog')



            
            

        

