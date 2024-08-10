from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.conf import settings
from django.contrib.auth.models import User
from .forms import *
from django.contrib import messages

def staffreg(r):
    if r.method=='POST':
            form=staff_form(r.POST)
            if form.is_valid():
                 form.save()
                 return redirect('admindb')
       
    else:
        form=staff_form()
        return render(r,'staffview/staffreg.html',{'form':form})

def stafflogin(r):
     print('hi')
     messages=" "
     if r.method=='POST':
          StaffId=r.POST.get('StaffId')
          password=r.POST.get('password')
          print(StaffId,password)
          try:
               staff12=staff.objects.get(StaffId=StaffId)
               print(staff12)
               print(staff12.password)
               if staff12.password == password:
                    r.session['StaffId'] = StaffId 
                    return redirect('staffdb')
               else:
                    print( 'Invalid Staff credentials')
          except staff.DoesNotExist:
               print('Invalid Staff credentials')
     else:
        print('welcome')
        form = staff_form()
        return render(r, 'staffview/stafflog.html', {'form': form})
def staffdashboard(r):
         if r.session.get('StaffId'):
               StaffId=r.session.get('StaffId')
               print(StaffId)
               staff12=staff.objects.get(StaffId=StaffId)
               print(staff12)
               return render(r,'staffview/staffdash.html',{'staff12':staff12})
         else:
              return redirect('stafflog')
def stafflogout(r):
    if 'StaffId' in r.session:
        del r.session['StaffId']  # Clear department ID from session
    return redirect('stafflog')
         
         
          
""" @login_required(login_url='/stafflogin/')
def stafflogout(r):
     logout(r)
     return redirect('stafflog') """
    
