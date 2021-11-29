import re
from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from django.views.decorators.clickjacking import xframe_options_exempt
from django.http import HttpResponseForbidden
from .login import *

def index(request):
        if(request.method == "POST"):
                stud_username = request.POST.get('student_username')
                stud_password = request.POST.get('student_password')
                if stud_username == 'admin' and stud_password == 'admin':
                        return student_portal(request)
        return render(request,'index.html')
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