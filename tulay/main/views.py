from django.http.response import HttpResponseNotFound
from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from django.http import Http404
from django.views.decorators.clickjacking import xframe_options_exempt
from django.http import HttpResponseForbidden
from .student_portal import *
from .teachers_portal import *
from .login import *

def error_404(request,exception):
        return HttpResponseNotFound("<h1>File Not Found</h1>")
def index(request):
        return HttpResponse("<script>window.location.assign('student_login_system/')</script>")
def login(request):
        if(request.method == "POST"):
                stud_username = request.POST.get('student_username')
                stud_password = request.POST.get('student_password')
                if stud_username == 'admin' and stud_password == 'admin':
                        return home_student_portal(request)
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

