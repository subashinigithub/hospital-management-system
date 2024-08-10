from django import forms
from .models import *
from django.contrib.auth.forms import AuthenticationForm

class hospitalform(forms.ModelForm):
    class Meta:
        model=hospital
        fields='__all__'
    
class doctorform(forms.ModelForm):
    class Meta:
        model=doctor
        fields=['Name','Age','Gender','Contact','AppointmentDate','AppointmentTime','Email','password','DoctorFee','photo']
        def clean(self):
            cleaned_data=super().clean()
            photo=cleaned_data.get('photo')
            if photo.size>1024*1024:
                raise forms.ValidationError('Image size may not exceed 5MB')
            if not(photo.image.format == 'JPEG' or photo.image.format == 'PNG'):
                raise forms.ValidationError('Photo format must be JPEG or PNG')
            return cleaned_data
        
class staff_form(forms.ModelForm):
    class Meta:
        model=staff
        fields='__all__'
        
class staff1(forms.ModelForm):
    StaffId=forms.CharField(max_length=255)
    password=forms.CharField(widget=forms.PasswordInput)

class patientform(forms.ModelForm):
    class Meta:
        model=patient
        fields='__all__'
       
class appointmentform(forms.ModelForm):
    class Meta:
        model=appointment
        fields='__all__'
        widgets = {
            'Doctor': forms.Select(attrs={'class': 'form-control'}),
            'ApointmentDate': forms.DateInput(attrs={'class': 'form-control'}),
            'ApointmentTime': forms.TimeInput(attrs={'class': 'form-control'}),
            'patient': forms.Select(attrs={'class': 'form-control'}),  # Change to Select for ForeignKey
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'Status': forms.TextInput(attrs={'class': 'form-control'}),
            'patient_phone': forms.TextInput(attrs={'class': 'form-control'}),
            'patient_name': forms.TextInput(attrs={'class': 'form-control'}),
        }

