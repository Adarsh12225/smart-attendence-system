from django.contrib import admin
from .models import Subject, ClassSession, Attendance

admin.site.register(Subject)
admin.site.register(ClassSession)
admin.site.register(Attendance)
