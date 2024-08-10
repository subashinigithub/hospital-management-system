from django.db import models
import os
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

class hospital(models.Model):
    Timing=models.TimeField(auto_now=False,null=True)
    Available=models.CharField(max_length=255)
    Rooms=models.CharField(max_length=255,null=True)
    session=models.CharField(max_length=255)
     
    def __str__(self) -> str:
        return str(self.Timing)
class doctor(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    Name=models.CharField(max_length=255)
    Age=models.PositiveIntegerField(null=True)
    Gender=models.CharField(max_length=100,null=True)
    Contact=models.CharField(max_length=255,null=True)
    AppointmentDate=models.DateField(null=True)
    AppointmentTime=models.TimeField(null=True)
    Email=models.EmailField(max_length=100,null=True,blank=True)
    password=models.CharField(max_length=255)
    specialist=models.CharField(max_length=255,null=True)
    DoctorFee=models.PositiveIntegerField()
    photo = models.ImageField(upload_to="images/", null=True, blank=True)

    def __str__(self) -> str:
        return self.Name

class staff(models.Model):
    StaffId=models.PositiveIntegerField()
    Name=models.CharField(max_length=255)
    Age=models.PositiveIntegerField()
    Gender=models.CharField(max_length=255,null=True)
    ShifTime=models.TimeField()
    ShiftName=models.CharField(max_length=255)
    Email=models.EmailField(max_length=100)
    password=models.CharField(max_length=255)
    Doctor=models.ForeignKey(doctor, on_delete=models.CASCADE, null=True, blank=True)
    Remarks=models.CharField(max_length=255,null=True)

    def __str__(self) -> str:
        return self.Name

class patient(models.Model):
    Name=models.CharField(max_length=255)
    Age=models.PositiveIntegerField()
    Gender=models.CharField(max_length=100,null=True)
    Contact=models.CharField(max_length=255,null=True)
    email=models.EmailField(max_length=100,null=True,blank=True)
    password=models.CharField(max_length=255)
    symptoms=models.CharField(max_length=255)
    Doctor=models.ForeignKey(doctor, on_delete=models.CASCADE, null=True, blank=True)
    medicalcertifcate=models.CharField(max_length=100,null=True)
    photo=models.ImageField(upload_to="images/", null=True, blank=True)
    Address=models.CharField(max_length=255,null=True)

    def __str__(self) -> str:
        return self.Name
    @property
    def get_photo_url(self):
            if self.photo and hasattr(self.photo, 'url'):
                return self.photo.url
            else:
                return "/static/images/user.jpg"
    
class appointment(models.Model):
     Doctor=models.ForeignKey(doctor, on_delete=models.CASCADE, null=True, blank=True)
     ApointmentDate=models.DateField()
     ApointmentTime=models.TimeField()
     patient=models.PositiveIntegerField()

     email=models.CharField(max_length=100,null=True)
     Status=models.CharField(max_length=255,null=True)
     patient_phone=models.CharField(max_length=100)
     patient_name=models.CharField(max_length=255)

     def __str__(self) ->str:
         return self.patient_name
     
     




    
















