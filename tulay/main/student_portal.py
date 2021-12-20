from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.clickjacking import xframe_options_sameorigin
def home_student_portal(request):
    return render(request,"home_student_portal.html")
def student_portal(request):
        return render(request,"student_portal.html")
def subject_student(request):
        return render(request,"subject_student.html")
def content_todo_student_portal(request):
        return render(request,"content_todo_student_portal.html")
def student_portal_student_status(request):
        return render(request,"student_portal_status.html")
def left_nav(request):
        return render(request,"left_nav.html")
def classroom_student_portal(request):
        return render(request,"classroom_student_portal.html")
def classroom_student_portal_frame(request):
        return render(request,"classroom_student_portal_frame.html")