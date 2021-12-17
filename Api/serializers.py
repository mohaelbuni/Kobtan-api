from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from Api.models import Task, Attendance, Student


# ----------------- user serializers -----------------------

class UserSerializer(serializers.ModelSerializer):
    isAdmin = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = User 
        fields = ('id','username','isAdmin',)
    
    def get_isAdmin(self,obj):
        return obj.is_staff
    


class UserSerializerWithToken(UserSerializer):
    token = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = User
        fields = ('id','username','isAdmin','token',)
    
    def get_token(self,obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token)
    
# --------------- Task serializers -----------------

class TaskSerializer(serializers.ModelSerializer):
    student_name = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Task
        fields = '__all__'
        
    def get_student_name(self,obj):
        student_name = str(obj.sid)
        return student_name
    def get_user_name(self,obj):
        user_name = str(obj.uid)
        return user_name
    
# ----------------- attendance serializers --------------------

class AttendanceSerializer(serializers.ModelSerializer):
    # token = serializers.SerializerMethodField(read_only=True)
    
    
    class Meta:
        model = Attendance
        fields = '__all__'
    

    
    
# ------------- Student serializer ------------------

class StudentSerializer(serializers.ModelSerializer):
    attendances = AttendanceSerializer(many=True,read_only=True)
    
    class Meta:
        model = Student
        fields = '__all__'
    

    
    

