from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.clickjacking import xframe_options_sameorigin

def teacher_portal(request):
        return render(request,"teachers_portal/teachersportal.html")
def teacher_nav_portal(request):
        return render(request,"teachers_portal/left_nav_teachers.html")
def subject(request):
        return render(request,"teachers_portal/subject.html")
def to_review_teachers_portal(request):
        return render(request,"teachers_portal/to_review_teachers_portal.html")
def content_todo_teachers_portal(request):
        return render(request,"teachers_portal/content_todo_teachers_portal.html")
def teachers_portal_grading_system(request):
        return render(request,"teachers_portal/grading_system.html")
def teachers_portal_grading_system_content(request):
        return render(request,"teachers_portal/grading_input.html")
def teachers_portal_student_status(request):
        return render(request,"teachers_portal/teachers_portal_student_status.html")
def export_data_grades(request):
        return render(request,"teachers_portal/export_data.html")
def teachers_portal_teachers_performance(request):
        return render(request,"teachers_portal/teachers_portal_teachers_performance.html")
