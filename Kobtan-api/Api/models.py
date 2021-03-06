from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


class Student(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255,blank=True,null=True)
    birth_date = models.DateField(blank=True,null=True)
    phone_number = PhoneNumberField(blank=True,null=True)
    
    def __str__(self):
        return self.name
    
    
class Attendance(models.Model):
    sid = models.ForeignKey(Student,on_delete=models.CASCADE,related_name='attendances')
    date = models.DateField()
    attend = models.BooleanField(default=False)
    
    def __str__(self):
        return str(self.date)
    
                   
class Task(models.Model):
    info = models.CharField(max_length=400,blank=True,null=True)
    sid = models.ForeignKey(Student,on_delete=models.CASCADE)
    uid = models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateField()
    creation_date= models.DateTimeField(auto_now_add=True)
    
    class Task_Type(models.TextChoices):
        READING = "READING"
        REVISION = "REVISION"
        WRITING = "WRITING"
    
    type = models.CharField(
    max_length=15, 
    choices = Task_Type.choices,
    default = Task_Type.READING
    )
    
    def __str__(self):
        return self.type
    
    
    
    
    