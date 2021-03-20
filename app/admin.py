from django.contrib import admin
from .models import Student, Hostel
from app.actions import showAllData

# Register your models here.

    
admin.site.register(Student)
admin.site.register(Hostel)

# This is showAllData from actions.py
admin.site.add_action(showAllData)