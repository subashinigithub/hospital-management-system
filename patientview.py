from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.conf import settings
from django.contrib.auth.models import User
from .forms import *
from django.contrib import messages

def patientreg(r):
    if r.method=='POST':
            form=patientform(r.POST,r.FILES)
            if form.is_valid():
                 form.save()
                 return redirect('patientdb')
       
    else:
        form=patientform()
        return render(r,'patientview/patientreg.html',{'form':form})

def patientlogin(r):
     print('hi')
     messages=""
     if r.method=='POST':
          email=r.POST.get('email')
          password=r.POST.get('password')
          print(email,password)
          try:
               patient1=patient.objects.get(email=email)
               print(patient1)
               print(patient1.password)
               if patient1.password == password:
                    r.session['ppk']=patient1.pk
                    r.session['email'] = email
                    return redirect('patientdb')
               else:
                    print( 'Invalid Staff credentials')
          except staff.DoesNotExist:
               print('Invalid Staff credentials')
     else:
        print('welcome')
        form = patientform()
        return render(r, 'patientview/patientlog.html', {'form': form})
     
def patientdashboard(r):
         if r.session.get('email'):
               email=r.session.get('email')
               print(email)
               patient1=patient.objects.get(email=email)
               print(patient1)
               return render(r,'patientview/patientdash.html',{'email':email})
         else:
              return redirect('patientlog')
         
def patientview(r):
        forms= patient.objects.all()
        return render(r, 'patientview/patientview.html', {'forms': forms})


def patientupdate(r,pk):
    app=appointment.objects.get(pk=pk)
    if r.method=='POST':
     form=appointmentform(r.POST,instance=app)
     print('hello')
     if form.is_valid():
          print('new')

          form.save()
          return redirect('patientdb')
     else:
          return render(r,'appointmentview/apposhow.html',{'forms':form})
    else:
     form=appointmentform(instance=app)
     
     return render(r,'patientview/patientupdate.html',{'forms':form})

         
def appointmentview1(r):
        pk=r.session.get('email')
        print(pk)
        forms=appointment.objects.filter(email=pk)
        
        return render(r, 'appointmentview/apposhow.html', {'forms': forms})

def patientlogout(r):
    if 'email' in r.session:
        del r.session['email']  # Clear department ID from session
    return redirect('patientlog')
        
       

