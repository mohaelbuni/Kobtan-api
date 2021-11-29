from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from Api.serializers import UserSerializer, UserSerializerWithToken, TaskSerializer, StudentSerializer, AttendanceSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.hashers import make_password
from rest_framework import status
from Api.models import Task, Attendance, Student

# ----- Users Routes -----

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
            is_staff=data['isAdmin']
            
        )
        serializer = UserSerializerWithToken(user, many=False)
        return Response(serializer.data)
    except:
        message = {'details': 'User with this email already exists!'}
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

# get all Task for a specific student, %% we need to add pagination to it.
@permission_classes([IsAuthenticated])
@api_view(['GET'])
def getTasks(request,student_id):
    tasks = Task.objects.filter(student_id=student_id)
    print(tasks)
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)

# get all attendance for specific date
@api_view(['GET'])
def getAttendances(request,date):
    attendances = Attendance.objects.filter(date=date)
    serializer = AttendanceSerializer(attendances, many=True)
    return Response(serializer.data)

# get sutdent by id
@api_view(['GET'])
def getStudent(request,student_id):
    students = Student.objects.filter(id=student_id)
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data)











