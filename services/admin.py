from django.contrib import admin

# Register your models here.
from services.models import Service, Doctor, Appoinment

admin.site.register(Service)
admin.site.register(Doctor)
admin.site.register(Appoinment)
