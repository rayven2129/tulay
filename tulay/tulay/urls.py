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
    path('student_login_system/',views.login),
    path("teachers_login_system/",views.teachers_login_system),
    path('enrollment_page1/',views.enrollmentsystem_page1),
    path('enrollment_page2/',views.enrollmentsystem_page2),
    path('menu/left_nav/',views.left_nav),
    path('menu/subject_student',views.subject_student),
    path('menu/student_portal',views.student_portal, name="Student Portal"),
    path('menu/teachers_portal',views.teacher_portal, name="Teacher Portal"),
    path('menu/teacher_nav_portal',views.teacher_nav_portal, name="Teacher_NavPortal"),
    path('menu/subject',views.subject),
    path('menu/content_todo_student_portal',views.content_todo_student_portal),
    path('menu/to_review_teachers_portal',views.to_review_teachers_portal),
    path('menu/content_todo_teachers_portal',views.content_todo_teachers_portal),
    path('menu/teachers_portal_grading_system',views.teachers_portal_grading_system),
    path('menu/teachers_portal_grading_system_content',views.teachers_portal_grading_system_content),
    path('menu/teachers_portal_student_status',views.teachers_portal_student_status),
    path('menu/student_portal_student_status',views.student_portal_student_status),
    path('menu/export_data_grades',views.export_data_grades),
    path('menu/teachers_portal_performance',views.teachers_portal_teachers_performance),

    
]