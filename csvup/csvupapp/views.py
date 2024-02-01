import csv
import datetime

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from csvupapp.EmailBackEnd import EmailBackEnd
from .models import *
import pandas as pd
from django.contrib.auth.hashers import make_password,check_password,get_hasher


def edit_adminpwd_save(request):
    if request.method!="POST":
        messages.error(request,"Task Failed")
        return HttpResponseRedirect("/admin_home/")
    else:
        ADMINid=int(request.session.get('keyid'))
        oldpassword=(request.POST.get("oldpassword"))
        newpassword=make_password(request.POST.get("newpassword"))
        try:
            user=CustomUser.objects.get(id=ADMINid)
            if check_password(oldpassword,user.password):
                user.password=newpassword
                user.save()
                messages.success(request,"Task Successful")
                return HttpResponseRedirect("/admin_home/")
            else:
                messages.error(request,"Task Failed")
                return HttpResponseRedirect("/admin_home/")
        except:
            messages.error(request,"Task Failed")
            return HttpResponseRedirect("/admin_home/")

def edit_pwd_save(request):
    if request.method!="POST":
        messages.error(request,"Task Failed")
        return HttpResponseRedirect("/student_home/")
    else:
        student_id=request.POST.get("student_id")
        oldpassword=request.POST.get("oldpassword")
        newpassword=request.POST.get("newpassword")
        try:
            user=CustomUser.objects.get(id=student_id)
            if check_password(oldpassword,user.password):
                user.password=make_password(newpassword)
                user.save()
                messages.success(request,"Task Successful")
                return HttpResponseRedirect("/student_home/")
            else:
                messages.error(request,"Task Failed")
                return HttpResponseRedirect("/student_home/")
        except:
            messages.error(request,"Task Failed")
            return HttpResponseRedirect("/student_home/")
# def create_db(file_path):
#     df = pd.read_csv(file_path,delimiter=',')
#     print(df.values)
#     list_csv=[list(row) for row in df.values]
#     for l in list_csv:
#         DataModel.objects.create(
#             id=l[0],
#             Name=l[1],
#             Age=l[2],
#             Email=l[3],
#             Address=l[4],
#         )
#
# def upload(request):
#     if request.method == 'POST':
#         file=request.FILES['file']
#         obj=File.objects.create(file=file)
#         create_db(obj.file)
#         return render(request,'uploadfile.html')
#     return render(request,'uploadfile.html')


def create_db(file_path):
    df = pd.read_csv(file_path,delimiter=',')
    print(df.values)
    list_csv=[list(row) for row in df.values]
    for l in list_csv:
        key=str(int(l[1]))
        prn=int(l[1])
        user=CustomUser.objects.create_user(username=l[0],password=key,email=l[0],last_name=l[5],first_name=l[3],user_type=3)
        user.students.prn=prn
        user.students.branch=l[2]
        user.students.middle_name=l[4]
        user.students.gender=l[6]
        dob=datetime.datetime.strptime(l[7],'%d-%m-%Y').strftime('%Y-%m-%d')
        user.students.date_of_birth=dob
        user.students.year_of_admission=l[8]
        user.students.type_of_admission=l[9]
        user.students.ssc_percentage=float(l[10])
        user.students.hsc_percentage=float(l[11])
        user.students.sgpa_fy_sem1=float(l[12])
        user.students.sgpa_fy_sem2=float(l[13])
        user.students.sgpa_sy_sem1=float(l[14])
        user.students.sgpa_sy_sem2=float(l[15])
        user.students.sgpa_ty_sem1=float(l[16])
        user.students.sgpa_ty_sem2=float(l[17])
        user.students.sgpa_btech_sem1=float(l[18])
        user.students.sgpa_btech_sem2=float(l[19])
        user.students.avg_elq_sy=float(l[20])
        user.students.avg_elq_ty=float(l[21])
        user.save()
def upload(request):
    if request.method == 'POST':
        file=request.FILES['file']
        obj=File.objects.create(file=file)
        try:
            create_db(obj.file)
            messages.success(request,"Task Successful")
            return HttpResponseRedirect("/admin_home/")
        except:
            messages.error(request,"Task Failed")
            return HttpResponseRedirect("/admin_home/")
    return HttpResponseRedirect("/admin_home/")

def download(request):
    adminid=int(request.session.get('keyid'))
    user=CustomUser.objects.all().exclude(id=adminid)
    Admintable=HttpResponse('')
    Admintable['Content-Disposition']='attachment;filename=Admintable.csv'
    writer1 = csv.writer(Admintable)
    writer1.writerow(["ID","College Email","First Name","Last Name"])
    admin_fields=user.values_list("id","email","first_name","last_name")
    for users in admin_fields:
        writer1.writerow(users)
    return Admintable

def download1(request):
    student=Students.objects.all()
    studenttable=HttpResponse('')
    studenttable['Content-Disposition']='attachment;filename=studenttable.csv'
    writer2 = csv.writer(studenttable)
    writer2.writerow(["ID","College Email","PRN (Permanent Registration Number)","Branch","Middle Name","Gender","Date Of Birth","Year of Admission","Type of Admission","Do you wish to get College Placements?","Opt-Out Form Placement (Undertaking)","Personal Email","LinkedIn Profile URL","Mobile Number","WhatsApp Number","Alternate Number","Father's Name ( Write NA if not Applicable )","Mother's Name","Permanent Address","Current/Correspondence Address","SSC (Class X) Percentage only  ( Do Not write % sign)","Are you a Diploma Student?","SGPA: SY Sem 1","SGPA: SY Sem 2","SGPA: TY Sem 1 ( Write NA if Awaiting)","SGPA: TY Sem 2 ( Write NA if Awaiting)","SGPA: BTech Sem 1 ( Write NA if Awaiting)","SGPA: BTech Sem 2 ( Write NA if Awaiting)","SGPA: FY Sem 1","SGPA: FY Sem 2","HSC (Class XII) Percentage","Diploma Percentage","Did you give AMCAT Exam in SY?","Did you give AMCAT Exam in TY?","Avg. ELQ Score in SY","Avg. ELQ Score in TY","Did you ever have any backlog?","Live/Pending Backlog Details	","Dead/Cleared Backlog Details","Completed Certification ","Other Completed Certifications	","Ongoing Certifications","Dropped Certifications","FY Summer Internship Program Details","SY Summer Internship or Project Details","TY Summer Internship, Project or Consultancy Details ","Sponsored Project - Industry (Title)","B.E. or Diploma Project (Title)","Open Elective - Specialisation","Programming Languages Known	","Frameworks Known	","Software Known","Additional Communication Languages Known","Co-curricular Activities (Top 3) ( Write NA if Not)","Special Achievements (State/National Level)","	Scholarship Availed","Additional Training Details","Extra Curricular Activities","Preskillet Video Interview Drive Link	","Passport Size Photo -- (Write Name_Branch_2023.Jpeg) this will easily make search ","SY AMCAT Result	","TY AMCAT Result","Industry Certifications - All Compiled	Educational Certifications - All Compiled","Internship Certifications - All Compiled","Certificate","Final AMCAT (SY)","Final AMCAT (TY)","AMCAT-1  YES/NO","AMCAT-2 YES/NO","Certification Yes / NO","Eligible Yes/NO","Awaiting"])
    student_fields=student.values_list("admin_id","college_email","prn","branch","middle_name","gender","date_of_birth","year_of_admission","type_of_admission","want_college_placement","out_placement","personal_email","linkedin_url","mobile_number","whatsapp_number","father_name","mother_name","permanent_address","current_address","ssc_percentage","diploma_student","sgpa_sy_sem1","sgpa_sy_sem2","sgpa_ty_sem1","sgpa_ty_sem2","sgpa_btech_sem1","sgpa_btech_sem2","sgpa_fy_sem1","sgpa_fy_sem2","hsc_percentage","diploma_percentage","gave_amcat_sy","gave_amcat_ty","avg_elq_sy","avg_elq_ty","have_backlog","live_backlog","dead_backlog","completed_certification","ongoing_certification","dropped_certification","fy_summer_internship","sy_summer_internship","ty_summer_internship","sponsored_project_industry","be_diploma_project_title","open_elective_specialisation","programming_languages_known","frameworks_known","software_known","languages_known","co_curricular_activities","special_achievements","scholarship","additional_details","extra_curricular_activities","preskillet_video_url","passport_size_url","sy_amcat_result_url","ty_amcat_result_url","all_industry_certification_url","all_education_certification_url","all_internship_certification_url","final_amcat_sy_url","final_amcat_ty_url","amcat_1","amcat_2","certification_done","eligible","awaiting")
    for students in student_fields:
        writer2.writerow(students)
    return studenttable

def temp(request):
    response=HttpResponse('')
    response['Content-Disposition']='attachment;filename=Template.csv'
    writer = csv.writer(response)
    writer.writerow(["Email Address(email)","PRN(float)","Branch","First Name","Middle Name","Last Name","Gender","Date Of Birth(date)","Year of Admission(int)","Type of Admission(char)","ssc_percentage","hsc_percentage","sgpa_fy_sem1","sgpa_fy_sem2","sgpa_sy_sem1","sgpa_sy_sem2","sgpa_ty_sem1","sgpa_ty_sem2","sgpa_btech_sem1","sgpa_btech_sem2","avg_elq_sy","avg_elq_ty"])
    return response

def ShowLoginPage(request):
    error=False
    if request.method!="POST":
        return render(request,"home.html",{})
    else:
        user=EmailBackEnd.authenticate(request,username=request.POST.get("email"),password=request.POST.get("password"))
        if user!=None:
            login(request,user)
            if user.user_type=="1":
                email=request.POST.get('email')
                user=CustomUser.objects.get(email=email)
                request.session['keyid']=user.id
                request.session['usertype']=user.user_type
                return HttpResponseRedirect('/admin_home/')
            elif user.user_type=="2":
                return HttpResponseRedirect(reverse("/staff_home/"))
            else:
                email=request.POST.get('email')
                user=CustomUser.objects.get(email=email)
                request.session['keyid']=user.id
                request.session['usertype']=user.user_type
                return HttpResponseRedirect("/student_home/")
        else:
            error=True
            return render(request,"home.html",{"error":error})


def GetUserDetails(request):
    if request.user!=None:
        return HttpResponse("User : "+request.user.email+" usertype : "+str(request.user.user_type))
    else:
        return HttpResponse("Please Login First")

def logout_user(request):
    if 'keyid' in request.session:
        del request.session['keyid']
    if 'usertype' in request.session:
        del request.session['usertype']
    logout(request)
    return HttpResponseRedirect("/")