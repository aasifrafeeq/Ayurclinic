from django.contrib import admin
from patients.models import *

# Register your models here.
admin.site.register(Patient)
admin.site.register(Medicine)