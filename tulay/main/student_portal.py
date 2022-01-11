from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.clickjacking import xframe_options_sameorigin
def home_student_portal(request):
    return render(request,"student_portal/home_student_portal.html")
def student_portal(request):
        return render(request,"student_portal/student_portal.html")
def subject_student(request):
        return render(request,"student_portal/subject_student.html")
def content_todo_student_portal(request):
        return render(request,"student_portal/content_todo_student_portal.html")
def student_portal_student_status(request):
        return render(request,"student_portal/student_portal_status.html")
def left_nav(request):
        return render(request,"student_portal/left_nav.html")
def classroom_student_portal(request):
        return render(request,"student_portal/classroom_student_portal.html")
def classroom_student_portal_frame(request):
        return render(request,"student_portal/classroom_student_portal_frame.html")
def student_browse_me (request):
        return render(request,"student_portal/student_browse_me.html")
def student_portal_message (request):
        return render(request, "student_portal/student_portal_messenger.html")
def subject_student_individual (request):
        return render(request, "student_portal/submission_subject_student_portal.html")
def submission_student_portal (request):
        return render(request,"student_portal/content_submission_student_portal.html")