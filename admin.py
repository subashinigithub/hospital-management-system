from django.contrib import admin
from .models import *

admin.site.register(hospital)
admin.site.register(doctor)
admin.site.register(staff)
admin.site.register(patient)
admin.site.register(appointment)


