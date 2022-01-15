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
from .enrollment_system_insert_database import *

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
        if (request.method == "POST"):
                student_status = request.POST.get('student_status')
                last_name = request.POST.get('last_name')
                first_name = request.POST.get('first_name')
                middle_name = request.POST.get('middle_name')
                gender_result = request.POST.get('gender_result')
                date_of_birth = request.POST.get('date_of_birth')
                place_of_birth = request.POST.get('place_of_birth')
                nationality_value = request.POST.get('nationality_value')
                religion_result = request.POST.get('religion_result')
                complete_address_line_one = request.POST.get('complete_address_line_one')
                complete_address_line_two = request.POST.get('complete_address_line_two')
                city_line_one = request.POST.get('city_line_one')
                province_line_one = request.POST.get('province_line_one')
                complete_address_line_one_completed = request.POST.get('complete_address_line_one_completed')
                complete_address_line_two_completed  = request.POST.get('complete_address_line_two_completed')
                city_line_two_completed = request.POST.get('city_line_two_completed')
                province_line_two_completed = request.POST.get('province_line_two_completed')
                contact_number = request.POST.get('contact_number')
                email_address = request.POST.get('email_address')
                enrollment_page_one_obj(
                                        student_status,
                                        last_name,
                                        first_name,
                                        middle_name,
                                        gender_result,
                                        date_of_birth,
                                        place_of_birth,
                                        nationality_value,
                                        religion_result,
                                        complete_address_line_one,
                                        complete_address_line_two,
                                        city_line_one,
                                        province_line_one,
                                        complete_address_line_one_completed,
                                        complete_address_line_two_completed,
                                        city_line_two_completed,
                                        province_line_two_completed,
                                        contact_number,
                                        email_address,
                                        )
                return enrollmentsystem_page2(request)

        return render(request,'enrollment_form/enrollmentsystem_page1.html')
def enrollmentsystem_page2(request):
        return render(request,'enrollment_form/enrollmentsystem_page2.html')

