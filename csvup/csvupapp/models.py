from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.
class File(models.Model):
    file = models.FileField(upload_to='abrahamapp/file',blank=True)

# class DataModel(models.Model):
#     Name=models.CharField(max_length=264,unique=True)
#     Age=models.IntegerField()
#     Email=models.EmailField(max_length=264,unique=True)
#     Address=models.CharField(max_length=264,unique=True)

class CustomUser(AbstractUser):
    user_type_data=((1,"HOD"),(2,"Staff"),(3,"Student"))
    user_type=models.CharField(default=1,choices=user_type_data,max_length=10)

class AdminHOD(models.Model):
    id=models.AutoField(primary_key=True)
    admin=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()

class Students(models.Model):
    id=models.AutoField(primary_key=True)
    Timestamp=models.DateTimeField(auto_now_add=True)
    admin=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    prn=models.BigIntegerField(validators=[MinValueValidator(1)],blank=True)
    branch=models.CharField(max_length=500,blank=True)
    middle_name=models.CharField(max_length=500,blank=True)
    gender=models.CharField(max_length=500,blank=True)
    date_of_birth=models.DateField(blank=True)
    year_of_admission=models.IntegerField(blank=True)
    type_of_admission=models.CharField(max_length=500,blank=True)
    want_college_placement=models.CharField(max_length=500,blank=True)
    out_placement=models.CharField(max_length=500,blank=True)
    personal_email=models.EmailField(max_length=500,blank=True)
    college_email=models.EmailField(max_length=500,blank=True)
    linkedin_url = models.URLField(max_length = 200,blank=True)
    mobile_number = models.BigIntegerField(validators=[MinValueValidator(0), MaxValueValidator(9999999999)],blank=True)
    whatsapp_number = models.BigIntegerField(validators=[MinValueValidator(0), MaxValueValidator(9999999999)],blank=True)
    alternate_number = models.BigIntegerField(validators=[MinValueValidator(0), MaxValueValidator(9999999999)],blank=True)
    father_name=models.CharField(max_length=500,blank=True)
    mother_name=models.CharField(max_length=500,blank=True)
    permanent_address=models.CharField(max_length=500,blank=True)
    current_address=models.CharField(max_length=500,blank=True)
    ssc_percentage=models.FloatField(validators=[MinValueValidator(0.00), MaxValueValidator(100.00)],blank=True)
    diploma_student=models.CharField(max_length=500,blank=True)
    sgpa_sy_sem1=models.FloatField(validators=[MinValueValidator(0.00), MaxValueValidator(10.00)],blank=True)
    sgpa_sy_sem2=models.FloatField(validators=[MinValueValidator(0.00), MaxValueValidator(10.00)],blank=True)
    sgpa_ty_sem1=models.FloatField(validators=[MinValueValidator(0.00), MaxValueValidator(10.00)],blank=True)
    sgpa_ty_sem2=models.FloatField(validators=[MinValueValidator(0.00), MaxValueValidator(10.00)],blank=True)
    sgpa_btech_sem1=models.FloatField(validators=[MinValueValidator(0.00), MaxValueValidator(10.00)],blank=True)
    sgpa_btech_sem2=models.FloatField(validators=[MinValueValidator(0.00), MaxValueValidator(10.00)],blank=True)
    sgpa_fy_sem1=models.FloatField(validators=[MinValueValidator(0.00), MaxValueValidator(10.00)],blank=True)
    sgpa_fy_sem2=models.FloatField(validators=[MinValueValidator(0.00), MaxValueValidator(10.00)],blank=True)
    hsc_percentage=models.FloatField(validators=[MinValueValidator(0.00), MaxValueValidator(100.00)],blank=True)
    diploma_percentage=models.FloatField(validators=[MinValueValidator(0.00), MaxValueValidator(100.00)],blank=True)
    gave_amcat_sy=models.CharField(max_length=500,blank=True)
    gave_amcat_ty=models.CharField(max_length=500,blank=True)
    avg_elq_sy=models.FloatField(validators=[MinValueValidator(0.00)],blank=True)
    avg_elq_ty=models.FloatField(validators=[MinValueValidator(0.00)],blank=True)
    have_backlog=models.CharField(max_length=500,blank=True)
    live_backlog=models.CharField(max_length=500,blank=True)
    dead_backlog=models.CharField(max_length=500,blank=True)
    completed_certification=models.CharField(max_length=500,blank=True)
    other_completed_certification=models.CharField(max_length=500,blank=True)
    ongoing_certification=models.CharField(max_length=500,blank=True)
    dropped_certification=models.CharField(max_length=500,blank=True)
    fy_summer_internship=models.CharField(max_length=500,blank=True)
    sy_summer_internship=models.CharField(max_length=500,blank=True)
    ty_summer_internship=models.CharField(max_length=500,blank=True)
    sponsored_project_industry=models.CharField(max_length=500,blank=True)
    be_diploma_project_title=models.CharField(max_length=500,blank=True)
    open_elective_specialisation=models.CharField(max_length=500,blank=True)
    programming_languages_known=models.CharField(max_length=500,blank=True)
    frameworks_known=models.CharField(max_length=500,blank=True)
    software_known=models.CharField(max_length=500,blank=True)
    languages_known=models.CharField(max_length=500,blank=True)
    co_curricular_activities=models.CharField(max_length=500,blank=True)
    special_achievements=models.CharField(max_length=500,blank=True)
    scholarship=models.CharField(max_length=500,blank=True)
    additional_details=models.CharField(max_length=500,blank=True)
    extra_curricular_activities=models.CharField(max_length=500,blank=True)
    preskillet_video_url = models.URLField(max_length = 200,blank=True)
    passport_size_url = models.URLField(max_length = 200,blank=True)
    sy_amcat_result_url = models.URLField(max_length = 200,blank=True)
    ty_amcat_result_url = models.URLField(max_length = 200,blank=True)
    all_industry_certification_url = models.URLField(max_length = 200,blank=True)
    all_education_certification_url = models.URLField(max_length = 200,blank=True)
    all_internship_certification_url = models.URLField(max_length = 200,blank=True)
    final_amcat_sy_url = models.URLField(max_length = 200,blank=True)
    final_amcat_ty_url = models.URLField(max_length = 200,blank=True)
    amcat_1=models.CharField(max_length=500,blank=True)
    amcat_2=models.CharField(max_length=500,blank=True)
    certification_done=models.CharField(max_length=500,blank=True)
    eligible=models.CharField(max_length=500,blank=True)
    awaiting=models.CharField(max_length=500,blank=True)
    objects = models.Manager()

@receiver(post_save,sender=CustomUser)
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        if instance.user_type==1:
            AdminHOD.objects.create(admin=instance)
        # if instance.user_type==2:
        #     Staffs.objects.create(admin=instance,address="")
        if instance.user_type==3:
            Students.objects.create(admin=instance,Timestamp="2023-01-01",gender="",branch="",prn=0,
            middle_name="",
            date_of_birth="2023-01-01",
            year_of_admission=2023,
            type_of_admission="",
            want_college_placement="",
            out_placement="",
            personal_email="",
            college_email="",
            linkedin_url = "",
            mobile_number = 0,
            whatsapp_number = 0,
            alternate_number = 0,
            father_name="",
            mother_name="",
            permanent_address="",
            current_address="",
            ssc_percentage=0,
            diploma_student="",
            sgpa_sy_sem1=0,
            sgpa_sy_sem2=0,
            sgpa_ty_sem1=0,
            sgpa_ty_sem2=0,
            sgpa_btech_sem1=0,
            sgpa_btech_sem2=0,
            sgpa_fy_sem1=0,
            sgpa_fy_sem2=0,
            hsc_percentage=0,
            diploma_percentage=0,
            gave_amcat_sy="",
            gave_amcat_ty="",
            avg_elq_sy=0,
            avg_elq_ty=0,
            have_backlog="",
            live_backlog="",
            dead_backlog="",
            completed_certification="",
            other_completed_certification="",
            ongoing_certification="",
            dropped_certification="",
            fy_summer_internship="",
            sy_summer_internship="",
            ty_summer_internship="",
            sponsored_project_industry="",
            be_diploma_project_title="",
            open_elective_specialisation="",
            programming_languages_known="",
            frameworks_known="",
            software_known="",
            languages_known="",
            co_curricular_activities="",
            special_achievements="",
            scholarship="",
            additional_details="",
            extra_curricular_activities="",
            preskillet_video_url = "",
            passport_size_url = "",
            sy_amcat_result_url = "",
            ty_amcat_result_url = "",
            all_industry_certification_url = "",
            all_education_certification_url = "",
            all_internship_certification_url = "",
            final_amcat_sy_url = "",
            final_amcat_ty_url = "",
            amcat_1="",
            amcat_2="",
            certification_done="",
            eligible="",
            awaiting="")

@receiver(post_save,sender=CustomUser)
def save_user_profile(sender,instance,**kwargs):
    if instance.user_type==1:
        instance.adminhod.save()
    # if instance.user_type==2:
    #     instance.staffs.save()
    if instance.user_type==3:
        instance.students.save()