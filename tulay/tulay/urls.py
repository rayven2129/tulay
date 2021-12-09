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
from main import student_portal
from main import teachers_portal
from django.urls import path
urlpatterns = [
    path('admin/', admin.site.urls),
    #---------------------{Index and Login System}---------------------#
    path('',views.index),
    path('student_login_system/',views.login),
    path("teachers_login_system/",views.teachers_login_system),
    path('enrollment_page1/',views.enrollmentsystem_page1),
    path('enrollment_page2/',views.enrollmentsystem_page2),
    #---------------------{For Student Portal}------------------------#
    path('menu/left_nav/',student_portal.left_nav),
    path('menu/subject_student',student_portal.subject_student),
    path('menu/student_portal',student_portal.student_portal, name="Student Portal"),
    path('menu/home_student_portal',student_portal.home_student_portal),
    path('menu/content_todo_student_portal',student_portal.content_todo_student_portal),
    path('menu/student_portal_student_status',student_portal.student_portal_student_status),
    #---------------------{For Teacher Portal}------------------------#
    path('menu/teachers_portal',teachers_portal.teacher_portal, name="Teacher Portal"),
    path('menu/teacher_nav_portal',teachers_portal.teacher_nav_portal, name="Teacher_NavPortal"),
    path('menu/subject',teachers_portal.subject),
    path('menu/to_review_teachers_portal',teachers_portal.to_review_teachers_portal),
    path('menu/content_todo_teachers_portal',teachers_portal.content_todo_teachers_portal),
    path('menu/teachers_portal_grading_system',teachers_portal.teachers_portal_grading_system),
    path('menu/teachers_portal_grading_system_content',teachers_portal.teachers_portal_grading_system_content),
    path('menu/teachers_portal_student_status',teachers_portal.teachers_portal_student_status),
    path('menu/export_data_grades',teachers_portal.export_data_grades),
    path('menu/teachers_portal_performance',teachers_portal.teachers_portal_teachers_performance),
    
]