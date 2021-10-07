from django.contrib import admin
from django.urls import path, re_path, include
from students import views
from students.models import Student
from students.serializers import StudentSerializer
from rest_framework import routers, viewsets

# class StudentViewSet(viewsets.ModelViewSet):  
#     serializer_class = StudentSerializer   
#     queryset = Student.objects.all()  

# router = routers.DefaultRouter()                   
# router.register(r'students', views.StudentViewSet, 'student') 

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # path('api/', include(router.urls)) 
    
    # re_path('api/students/', views.getAllStudents),
    # re_path('api/students/<int:pk>', views.getStudent),
    
    path(r'api/students/', views.students_list),
    path(r'api/students/<int:pk>/', views.students_detail),
    
    # re_path(r'^api/students/$', views.getAllStudents),
    # re_path(r'^api/students/([0-9])$', views.getStudent),
]