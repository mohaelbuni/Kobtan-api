from django.core.checks import messages
from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from Api.serializers import UserSerializer, UserSerializerWithToken, TaskSerializer, StudentSerializer, AttendanceSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.hashers import make_password
from rest_framework import serializers, status
from Api.models import Task, Attendance, Student
import datetime

# ==============================
# ======== Users Routes ========
# ==============================

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        serializer = UserSerializerWithToken(self.user).data

        for k, v in serializer.items():
            data[k] = v

        return data


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

# this is for Register new user
@api_view(['POST'])
def registerUser(request):
    data = request.data
    try:
        user = User.objects.create(
            username=data['username'],
            password=make_password(data['password']),
            is_staff=False
            
        )
        serializer = UserSerializerWithToken(user, many=False)
        return Response(serializer.data)
    except:
        message = {'details': 'something went wrong!!!, maybe email already exists!'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)

# this is for get user profile information, works only for Authenticated user
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUserProfile(request):
    user = request.user
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)

# get all users this is for admin
@api_view(['GET'])
@permission_classes([IsAdminUser])
def getUsers(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

# ================================
# ======== Student Routes ========
# ================================

# get all sutdents 
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getAllStudents(request):
    students = Student.objects.all()
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data)

# get sutdent by id
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getStudentById(request,student_id):
    student = Student.objects.get(id=student_id)
    serializer = StudentSerializer(student, many=False)
    return Response(serializer.data)

# add student
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addStudent(request):
    data = request.data
    try:
        student = Student(name=data['name'])
        student.save()
        print(student)
        serializer = StudentSerializer(student, many=False)
        return Response({"info":"Added Successfully👍👍","student": serializer.data})
    except:
        message = {'details': 'something went wrong!!!,'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)  
 
# delete student   
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteStudent(request,student_id):
    try:
        student = Student.objects.get(id=student_id)
        student.delete()
        return Response({"info":"deleted Successfully👍👍"})
    except:
        message = {'details': 'something went wrong!!!,'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)  

# update Student   
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateStudent(request,student_id):
    data = request.data

    print(data)
    try:
        student = Student.objects.get(id=student_id)
        
        for (key,value) in data.items():
            setattr(student, key, value)
        
        student.save()
        serializer = StudentSerializer(student,many=False)
        return Response({"info":"updated Successfully👍👍","student":serializer.data})
    except:
        message = {'details': 'something went wrong!!!,'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)  
    
# ====================================
# ======== Attendances Routes ========
# ====================================

# add list of students attendance
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addAttendList(request):   
    date = request.data['date'] 
    for sid in request.data['attend']:
        try:
            student = Student.objects.get(id=sid)
        except Student.DoesNotExist:
            message = {'details': f'Student with (id:{sid}) does not exists!!,'}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)   
    for sid in request.data['attend']:
        try:
            att = Attendance.objects.get(sid=sid)
            continue
        except Attendance.DoesNotExist:
            attend = Attendance(sid=student,date=date,attend=True)
            attend.save()

    return Response({"info":"attendances added Successfully👍👍"})  

#  Remove list of students attendance
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def removeAttend(request):
    date = request.data['date'] 
    for sid in request.data['attend']:
        try:
            student = Student.objects.get(id=sid)
        except Student.DoesNotExist:
            message = {'details': f'Student with (id:{sid}) does not exists!!,'}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)
    for sid in request.data['attend']:
        try:
            attend = Attendance.objects.filter(sid=sid,date=date)
            attend.delete()
        except Attendance.DoesNotExist:
            continue

    return Response({"info":"attendances added Successfully👍👍"})  

# get all attendances by date
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getAttendByDate(request,date):
    attendances = Attendance.objects.filter(date=date)
    serializer = AttendanceSerializer(attendances, many=True)
    return Response(serializer.data)

# ================================
# ======== Tasks Routes ==========
# ================================

# add student Task
# update student Task
# remove student Task
# Get the last task by type
# Get all student tasks by student_id must be paginated

# get all Task for a specific student, %% we need to add pagination to it.
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getAllStudentTasks(request,student_id):
    tasks = Task.objects.filter(student_id=student_id)
    print(tasks)
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)










