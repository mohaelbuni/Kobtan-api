from rest_framework_simplejwt.views import TokenRefreshView
from django.urls import path
from Api.views import user_views as views 

urlpatterns = [
    # users urls
    path('register/', views.registerUser, name='register'),
    path('login/', views.MyTokenObtainPairView.as_view() , name='token_obtain_pair'),
    path('users/', views.getUsers, name='users'),
    path('profile/', views.getUserProfile, name='users-profile'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # students urls
    path('students/',views.getAllStudents , name='all-student'),
    path('student/<int:student_id>',views.getStudentById , name='student'),
    path('student/add',views.addStudent , name='add-student'),
    path('student/delete/<int:student_id>',views.deleteStudent , name='delete-student'),
    path('student/update/<int:student_id>',views.updateStudent , name='update-student'),
    
    
    
    # tasks urls
    path('student/<int:student_id>/tasks/',views.getAllStudentTasks , name='tasks'),
    # attendances urls
    path('attend/add',views.addAttendList , name='add-attend'),
    path('attend/remove',views.removeAttend , name='remove-attend'),
    path('attend/<str:date>',views.getAttendByDate , name='attend'),
    
]
