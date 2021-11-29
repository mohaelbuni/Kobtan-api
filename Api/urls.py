from rest_framework_simplejwt.views import TokenRefreshView
from django.urls import path
from Api.views import user_views as views 

urlpatterns = [
    path('', views.getUsers, name='users'),
    path('register/', views.registerUser, name='register'),
    path('login/', views.MyTokenObtainPairView.as_view() , name='token_obtain_pair'),
    path('profile/', views.getUserProfile, name='users-profile'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # task urls
    path('tasks/<int:student_id>',views.getTasks , name='tasks'),
    path('attendances/<str:date>',views.getAttendances , name='tasks'),
    path('student/<int:student_id>',views.getStudent , name='tasks'),
]
