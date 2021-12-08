from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from django.views.decorators.clickjacking import xframe_options_exempt
from django.http import HttpResponseForbidden
from .login import *
def index(request):
        return HttpResponse("<script>window.location.assign('student_login_system/')</script>")
def login(request):
        if(request.method == "POST"):
                stud_username = request.POST.get('student_username')
                stud_password = request.POST.get('student_password')
                if stud_username == 'admin' and stud_password == 'admin':
                        
                        return student_portal(request)
        return render(request,'index.html')
def teachers_login_system(request):
        if (request.method == "POST"):
                teachers_username = request.POST.get('teachers_username')
                teachers_password = request.POST.get('teachers_password')
                if teachers_username == 'user' and teachers_password == 'password':
                        return teacher_portal(request)
                else:
                        return render(request,"teachers_login_portal.html")

        return render(request,"teachers_login_portal.html")
def enrollmentsystem_page1(request):
        return render(request,'enrollmentsystem_page1.html')
def enrollmentsystem_page2(request):
        return render(request,'enrollmentsystem_page2.html')
def left_nav(request):
        return render(request,"left_nav.html")
def subject_student(request):
        return render(request,"subject_student.html")
def student_portal(request):
        return render(request,"student_portal.html")
def teacher_portal(request):
        return render(request,"teachersportal.html")
def teacher_nav_portal(request):
        return render(request,"left_nav_teachers.html")
def subject(request):
        return render(request,"subject.html")
def content_todo_student_portal(request):
        return render(request,"content_todo_student_portal.html")
def to_review_teachers_portal(request):
        return render(request,"to_review_teachers_portal.html")
def content_todo_teachers_portal(request):
        return render(request,"content_todo_teachers_portal.html")
def teachers_portal_grading_system(request):
        return render(request,"grading_system.html")
def teachers_portal_grading_system_content(request):
        return render(request,"grading_input.html")
def teachers_portal_student_status(request):
        return render(request,"teachers_portal_student_status.html")
def student_portal_student_status(request):
        return render(request,"student_portal_status.html")
def export_data_grades(request):
        return render(request,"export_data.html")
def teachers_portal_teachers_performance(request):
        return render(request,"teachers_portal_teachers_performance.html")