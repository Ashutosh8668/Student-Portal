from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import *
from django.contrib.auth.hashers import make_password,check_password


def student_home(request):
    usertype=int(request.session.get('usertype'))
    if usertype == 3:
        studentid=int(request.session.get('keyid'))
        user=CustomUser.objects.get(id=studentid)
        student=Students.objects.get(admin=studentid)
        username=user.first_name
        studentprn=student.prn
        ssc=student.ssc_percentage
        sscnot=round(100-ssc,2)
        hsc=student.hsc_percentage
        hscnot=round(100-ssc,2)
        fy1=student.sgpa_fy_sem1
        fy2=student.sgpa_fy_sem2
        sy1=student.sgpa_sy_sem1
        sy2=student.sgpa_sy_sem2
        ty1=student.sgpa_ty_sem1
        ty2=student.sgpa_ty_sem2
        btech1=student.sgpa_btech_sem1
        btech2=student.sgpa_btech_sem2
        elqs=student.avg_elq_sy
        elqt=student.avg_elq_ty
        values= {
            'ssc':ssc,
            'sscnot':sscnot,
            'hsc':hsc,
            'hscnot':hscnot,
            'fy1':fy1,
            'fy2':fy2,
            'sy1':sy1,
            'sy2':sy2,
            'ty1':ty1,
            'ty2':ty2,
            'btech1':btech1,
            'btech2':btech2,
            'elqs':elqs,
            'elqt':elqt
        }
        return render(request,"welcome.html",{"username":username,"student":student,"studentid":studentid,"values":values,"studentprn":studentprn})
    else:
        return HttpResponseRedirect("/")

def updateplacement(request):
    if request.method!="POST":
        return HttpResponseRedirect("/student_home/")
    else:
        want_college_placement=request.POST.get("want_college_placement")
        out_placement=request.POST.get("out_placement")
        personal_email=request.POST.get("personal_email")
        college_email=request.POST.get("college_email")
        gave_amcat_sy=request.POST.get("gave_amcat_sy")
        gave_amcat_ty=request.POST.get("gave_amcat_ty")
        diploma_student=request.POST.get("diploma_student")
        diploma_percentage=request.POST.get("diploma_percentage")
        diploma_percentage=request.POST.get("diploma_percentage")
        student_id=request.POST.get("student_id")
        try:
            student_model=Students.objects.get(admin=student_id)
            student_model.want_college_placement=want_college_placement
            student_model.out_placement=out_placement
            student_model.personal_email=personal_email
            student_model.college_email=college_email
            student_model.gave_amcat_sy=gave_amcat_sy
            student_model.gave_amcat_ty=gave_amcat_ty
            student_model.diploma_percentage=float(diploma_percentage)
            student_model.diploma_student=diploma_student
            student_model.save()
            messages.success(request,"Successfully Inserted")
            return HttpResponseRedirect("/student_home/")
        except:
            messages.error(request,"Failed to Insert")
            return HttpResponseRedirect("/student_home/")

def updategrades(request):
    if request.method!="POST":
        return HttpResponseRedirect("/student_home/")
    else:
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
        student_id=request.POST.get("student_id")
        try:
            student_model=Students.objects.get(admin=student_id)
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
            messages.success(request,"Successfully Inserted")
            return HttpResponseRedirect("/student_home/")
        except:
            messages.error(request,"Failed to Insert")
            return HttpResponseRedirect("/student_home/")

def updatenumbers(request):
    if request.method!="POST":
        return HttpResponseRedirect("/student_home/")
    else:
        alternate_number=request.POST.get("alternate_number")
        mobile_number=request.POST.get("mobile_number")
        whatsapp_number=request.POST.get("whatsapp_number")
        student_id=request.POST.get("student_id")
        try:
            student_model=Students.objects.get(admin=student_id)
            student_model.mobile_number=int(mobile_number)
            student_model.whatsapp_number=int(whatsapp_number)
            student_model.alternate_number=int(alternate_number)
            student_model.save()
            messages.success(request,"Successfully Inserted")
            return HttpResponseRedirect("/student_home/")
        except:
            messages.error(request,"Failed to Insert")
            return HttpResponseRedirect("/student_home/")


def updateurls(request):
    if request.method!="POST":
        return HttpResponseRedirect("/student_home/")
    else:
        linkedin_url=request.POST.get("linkedin_url")
        preskillet_video_url=request.POST.get("preskillet_video_url")
        passport_size_url=request.POST.get("passport_size_url")
        sy_amcat_result_url=request.POST.get("sy_amcat_result_url")
        ty_amcat_result_url=request.POST.get("ty_amcat_result_url")
        all_industry_certification_url=request.POST.get("all_industry_certification_url")
        all_education_certification_url=request.POST.get("all_education_certification_url")
        all_internship_certification_url=request.POST.get("all_internship_certification_url")
        final_amcat_sy_url=request.POST.get("final_amcat_sy_url")
        final_amcat_ty_url=request.POST.get("final_amcat_ty_url")
        student_id=request.POST.get("student_id")
        try:
            student_model=Students.objects.get(admin=student_id)
            student_model.linkedin_url=linkedin_url
            student_model.preskillet_video_url=preskillet_video_url
            student_model.passport_size_url=passport_size_url
            student_model.sy_amcat_result_url=sy_amcat_result_url
            student_model.ty_amcat_result_url=ty_amcat_result_url
            student_model.all_industry_certification_url=all_industry_certification_url
            student_model.all_education_certification_url=all_education_certification_url
            student_model.all_internship_certification_url=all_internship_certification_url
            student_model.final_amcat_sy_url=final_amcat_sy_url
            student_model.final_amcat_ty_url=final_amcat_ty_url
            student_model.save()
            messages.success(request,"Successfully Inserted")
            return HttpResponseRedirect("/student_home/")
        except:
            messages.error(request,"Failed to Insert")
            return HttpResponseRedirect("/student_home/")


def updatepersonals(request):
    if request.method!="POST":
        return HttpResponseRedirect("/student_home/")
    else:
        father_name=request.POST.get("father_name")
        mother_name=request.POST.get("mother_name")
        permanent_address=request.POST.get("permanent_address")
        current_address=request.POST.get("current_address")
        have_backlog=request.POST.get("have_backlog")
        live_backlog=request.POST.get("live_backlog")
        dead_backlog=request.POST.get("dead_backlog")
        student_id=request.POST.get("student_id")
        try:
            student_model=Students.objects.get(admin=student_id)
            student_model.father_name=father_name
            student_model.mother_name=mother_name
            student_model.permanent_address=permanent_address
            student_model.current_address=current_address
            student_model.have_backlog=have_backlog
            student_model.live_backlog=live_backlog
            student_model.dead_backlog=dead_backlog
            student_model.save()
            messages.success(request,"Successfully Inserted")
            return HttpResponseRedirect("/student_home/")
        except:
            messages.error(request,"Failed to Insert")
            return HttpResponseRedirect("/student_home/")

def updateskills(request):
    if request.method!="POST":
        return HttpResponseRedirect("/student_home/")
    else:
        completed_certification=request.POST.get("completed_certification")
        other_completed_certification=request.POST.get("other_completed_certification")
        ongoing_certification=request.POST.get("ongoing_certification")
        dropped_certification=request.POST.get("dropped_certification")
        fy_summer_internship=request.POST.get("fy_summer_internship")
        sy_summer_internship=request.POST.get("sy_summer_internship")
        ty_summer_internship=request.POST.get("ty_summer_internship")
        sponsored_project_industry=request.POST.get("sponsored_project_industry")
        be_diploma_project_title=request.POST.get("be_diploma_project_title")
        open_elective_specialisation=request.POST.get("open_elective_specialisation")
        programming_languages_known=request.POST.get("programming_languages_known")
        frameworks_known=request.POST.get("frameworks_known")
        software_known=request.POST.get("software_known")
        languages_known=request.POST.get("languages_known")
        co_curricular_activities=request.POST.get("co_curricular_activities")
        special_achievements=request.POST.get("special_achievements")
        scholarship=request.POST.get("scholarship")
        additional_details=request.POST.get("additional_details")
        extra_curricular_activities=request.POST.get("extra_curricular_activities")
        certification_done=request.POST.get("certification_done")
        student_id=request.POST.get("student_id")
        try:
            student_model=Students.objects.get(admin=student_id)
            student_model.completed_certification=completed_certification
            student_model.other_completed_certification=other_completed_certification
            student_model.ongoing_certification=ongoing_certification
            student_model.dropped_certification=dropped_certification
            student_model.fy_summer_internship=fy_summer_internship
            student_model.sy_summer_internship=sy_summer_internship
            student_model.ty_summer_internship=ty_summer_internship
            student_model.sponsored_project_industry=sponsored_project_industry
            student_model.be_diploma_project_title=be_diploma_project_title
            student_model.open_elective_specialisation=open_elective_specialisation
            student_model.programming_languages_known=programming_languages_known
            student_model.frameworks_known=frameworks_known
            student_model.software_known=software_known
            student_model.languages_known=languages_known
            student_model.co_curricular_activities=co_curricular_activities
            student_model.special_achievements=special_achievements
            student_model.scholarship=scholarship
            student_model.additional_details=additional_details
            student_model.certification_done=certification_done
            student_model.extra_curricular_activities=extra_curricular_activities
            student_model.save()
            messages.success(request,"Successfully Inserted")
            return HttpResponseRedirect("/student_home/")
        except:
            messages.error(request,"Failed to Insert")
            return HttpResponseRedirect("/student_home/")