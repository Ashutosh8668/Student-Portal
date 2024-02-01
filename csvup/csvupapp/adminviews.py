from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import *
from django.contrib.auth.hashers import make_password
# from abrahamapp.forms import AddStudentForm, EditStudentForm
# from abrahamapp.models import CustomUser, Staffs, Courses, Subjects, Students


def admin_home(request):
    usertype=int(request.session.get('usertype'))
    if usertype == 1:
        many=True
        one=False
        student=Students.objects.all()
        return render(request,"welcome_admin.html",{"student":student,"many":many,"one":one})
    else:
        return HttpResponseRedirect("/")


def all_out(request):
    try:
        student=Students.objects.all()
        student.delete()
        adminid=int(request.session.get('keyid'))
        user=CustomUser.objects.all().exclude(id=adminid)
        user.delete()
        messages.success(request,"Task Successful")
        return HttpResponseRedirect("/admin_home/")
    except:
        messages.error(request,"Task Failed")
        return HttpResponseRedirect("/admin_home/")


def delete_student_save(request,student_id):
    try:
        student=Students.objects.get(admin=student_id)
        student.delete()
        user=CustomUser.objects.get(id=student_id)
        user.delete()
        messages.success(request,"Task Successful")
        return HttpResponseRedirect("/admin_home/")
    except:
        messages.error(request,"Task Failed")
        return HttpResponseRedirect("/admin_home/")




def edit_student(request,student_id):
    student=Students.objects.get(admin=student_id)
    return render(request,"update_student_form.html",{"student":student,"id":student_id})

def edit_student_save(request):
    if request.method!="POST":
        messages.error(request,"Task Failed")
        return HttpResponseRedirect("/admin_home/")
    else:
        student_id=request.POST.get("student_id")
        prn=request.POST.get("prn")
        first_name=request.POST.get("first_name")
        middle_name=request.POST.get("middle_name")
        last_name=request.POST.get("last_name")
        email=request.POST.get("email")
        branch=request.POST.get("branch")
        gender=request.POST.get("gender")
        date_of_birth=request.POST.get("date_of_birth")
        year_of_admission=request.POST.get("year_of_admission")
        type_of_admission=request.POST.get("type_of_admission")
        ssc_percentage=request.POST.get("ssc_percentage")
        hsc_percentage=request.POST.get("hsc_percentage")
        sgpa_fy_sem1=request.POST.get("sgpa_fy_sem1")
        sgpa_fy_sem2=request.POST.get("sgpa_fy_sem2")
        sgpa_sy_sem1=request.POST.get("sgpa_sy_sem1")
        sgpa_sy_sem2=request.POST.get("sgpa_sy_sem2")
        sgpa_ty_sem1=request.POST.get("sgpa_ty_sem1")
        sgpa_ty_sem2=request.POST.get("sgpa_ty_sem2")
        sgpa_btech_sem1=request.POST.get("sgpa_btech_sem1")
        sgpa_btech_sem2=request.POST.get("sgpa_btech_sem2")
        avg_elq_sy=request.POST.get("avg_elq_sy")
        avg_elq_ty=request.POST.get("avg_elq_ty")

        try:
            user=CustomUser.objects.get(id=student_id)
            user.first_name=first_name
            user.last_name=last_name
            user.email=email
            user.save()

            student_model=Students.objects.get(admin=student_id)
            student_model.middle_name=middle_name
            student_model.prn=float(prn)
            student_model.branch=branch
            student_model.gender=gender
            student_model.date_of_birth=date_of_birth
            student_model.year_of_admission=int(year_of_admission)
            student_model.type_of_admission=type_of_admission
            student_model.ssc_percentage=float(ssc_percentage)
            student_model.hsc_percentage=float(hsc_percentage)
            student_model.sgpa_fy_sem1=float(sgpa_fy_sem1)
            student_model.sgpa_fy_sem2=float(sgpa_fy_sem2)
            student_model.sgpa_sy_sem1=float(sgpa_sy_sem1)
            student_model.sgpa_sy_sem2=float(sgpa_sy_sem2)
            student_model.sgpa_ty_sem1=float(sgpa_ty_sem1)
            student_model.sgpa_ty_sem2=float(sgpa_ty_sem2)
            student_model.sgpa_btech_sem1=float(sgpa_btech_sem1)
            student_model.sgpa_btech_sem2=float(sgpa_btech_sem2)
            student_model.avg_elq_sy=float(avg_elq_sy)
            student_model.avg_elq_ty=float(avg_elq_ty)
            student_model.save()
            messages.success(request,"Task Successful")
            return HttpResponseRedirect("/admin_home/")
        except:
            messages.error(request,"Task Failed")
            return HttpResponseRedirect("/admin_home/")


def add_student_save(request):
    if request.method!="POST":
        return HttpResponseRedirect("/admin_home/")
    else:
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        username=request.POST.get("email")
        email=request.POST.get("email")
        password=request.POST.get("password")
        current_address=request.POST.get("current_address")
        prn=request.POST.get("prn")
        try:
            user=CustomUser.objects.create_user(username=username,password=password,email=email,last_name=last_name,first_name=first_name,user_type=3)
            user.students.current_address=current_address
            user.students.prn=prn
            user.save()
            messages.success(request,"Task Successful")
            return HttpResponseRedirect("/admin_home/")
        except:
            messages.error(request,"Task Failed")
            return HttpResponseRedirect("/admin_home/")

