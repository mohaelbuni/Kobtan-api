from django.contrib import admin
from django.contrib.auth.models import User
from Api import models
# Register your models here.


# admin.site.register(User)
admin.site.register(models.Student)
admin.site.register(models.Task)
# admin.site.register(models.TaskType)
admin.site.register(models.Attendance)