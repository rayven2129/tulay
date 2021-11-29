"""tulay URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from main import views 
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('enrollment_page1/',views.enrollmentsystem_page1),
    path('enrollment_page2/',views.enrollmentsystem_page2),
    path('menu/left_nav/',views.left_nav),
    path('menu/subject_student',views.subject_student),
    path('menu/student_portal',views.student_portal, name="Student Portal"),
    path('menu/teachers_portal',views.teacher_portal, name="Teacher Portal"),
    path('menu/teacher_nav_portal',views.teacher_nav_portal, name="Teacher_NavPortal"),
    
]
