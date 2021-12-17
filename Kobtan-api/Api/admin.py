from django.contrib import admin
from django.contrib.auth.models import User
from Api.models import Student, Task, Attendance
# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ('name','id','address','birth_date','phone_number')
    ordering =('id',)

class TaskAdmin(admin.ModelAdmin):
    list_display  = ('type','sid', 'uid','date')
    list_filter = ('date',)
    ordering =('-date',)
    
    

class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('sid','attend','date')
    ordering =('-date',)

admin.site.register(Student,StudentAdmin)
admin.site.register(Task,TaskAdmin)
admin.site.register(Attendance,AttendanceAdmin)