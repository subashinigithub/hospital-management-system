from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.conf import settings
from django.contrib.auth.models import User
from .forms import *
from django.contrib import messages
from .models import *
def appointmentreg(r):
    Doctor=doctor.objects.all()
    if r.method=='POST':
            form=appointmentform(r.POST)

            doc=r.POST["Doctor"]
            d=doctor.objects.get(Name=doc)
            print(d)

            apd=r.POST["ApointmentDate"]
            apt=r.POST["ApointmentTime"]
            print(doc,apd,apt)
            email=r.session.get('email')
            patient1=patient.objects.get(email=email)
            name=patient1.Name
            phno=patient1.Contact
            app=appointment.objects.create(Doctor=d,ApointmentDate=apd,ApointmentTime=apt,patient=1,email=email,Status="active",patient_phone=phno,patient_name=name)
            app.save()
            return redirect('patientdb')

          
       
    else:
        form=appointmentform()
        return render(r,'appointmentview/apporeg.html',{'form':form, 'Doctor':Doctor})


def appointmentview(r):
        forms= appointment.objects.all()
        return render(r, 'appointmentview/appoview.html', {'forms': forms})
      