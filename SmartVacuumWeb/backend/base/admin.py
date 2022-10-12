from django.contrib import admin
from .models import Sensor, Status
# Register your models here.

admin.site.register(Status)
admin.site.register(Sensor)