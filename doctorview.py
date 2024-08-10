from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.conf import settings
from django.contrib.auth.models import User
from .forms import *

def docregister(r):
    if r.user.is_authenticated and r.user.is_staff:
        if r.method=='POST':
            form=doctorform(r.POST,r.FILES)
            if form.is_valid():
                doctor=form.save(commit=False)
                email=form.cleaned_data['Email']
                password=form.cleaned_data['password']
                user=User.objects.create_user(username=email,email=email,password=password)
                doctor.user=user
                doctor.save()
            return redirect('docdb')
        else:
            form=doctorform()
        return render(r,'doctorview/docreg.html',{'form':form})
    else:
        return redirect('doclog')
def docdashboard(r):
    if r.user.is_authenticated and not(r.user.is_staff):
        return render(r,'doctorview/doctordash.html')
    else:
        return redirect('doclog')
    
""" def doctorview(r):
        forms= appointment.objects.all()
       
        n=r.user.username
        print(n)
        return render(r, 'doctorview/doctorview.html', {'forms': forms}) """

from django.shortcuts import render, redirect
from .models import appointment  # Assuming you have an Appointment model

def doctorview(r):
    if r.user.is_authenticated and not r.user.is_staff:
        forms = appointment.objects.all()
        n = r.user.username
        dc=doctor.objects.get(Email=n)
        print(dc)
        print(f"Authenticated username: {n}")  # Added f-string for clarity
        return render(r, 'doctorview/doctorview.html', {'forms': forms, 'username': dc})
    else:
        return redirect('doclog')


def doctorlogin(r):
    if r.user.is_authenticated and not(r.user.is_staff):
        return redirect('docdb')
    message=""
    if r.method == 'POST':
        email=r.POST.get('email')
        password=r.POST.get('password')
        print(email,password)
        user=authenticate(r,username=email,password=password)
        print(user)
        if user is not None:
            login(r,user)
            return redirect('docdb')
        else:
            message="Invalid emailId or password"
    else:
        form=doctorform()
    return render(r,'doctorview/doclog.html',{'message':message})

    

@login_required(login_url='/doclogin/')
def doclogout(r):
    logout(r)
    return redirect('doclog')
