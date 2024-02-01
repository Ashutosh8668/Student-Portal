"""csvup URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from csvupapp import views, adminviews,studentviews
from csvup import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.ShowLoginPage,name="show_login/"),
    path('upload/',views.upload,name="upload/"),
    path('download/',views.download,name="download/"),
    path('download1/',views.download1,name="download1/"),
    path('temp/',views.temp,name="temp/"),
    path('get_user_details/', views.GetUserDetails),
    path('logout_user/', views.logout_user,name="logout/"),
    path('admin_home/',adminviews.admin_home,name="admin_home/"),
    path('student_home/',studentviews.student_home,name="student_home/"),
    path('updateplacement/',studentviews.updateplacement,name="updateplacement/"),
    path('updategrades/',studentviews.updategrades,name="updategrades/"),
    path('updatenumbers/',studentviews.updatenumbers,name="updatenumbers/"),
    path('updateurls/',studentviews.updateurls,name="updateurls/"),
    path('updatepersonals/',studentviews.updatepersonals,name="updatepersonals/"),
    path('updateskills/',studentviews.updateskills,name="updateskills/"),
    path('add_student_save/',adminviews.add_student_save,name="add_student_save/"),
    path('edit_student/<str:student_id>',adminviews.edit_student,name="edit_student"),
    path('edit_student_save/',adminviews.edit_student_save,name="edit_student/"),
    path('edit_pwd_save/',views.edit_pwd_save,name="edit_pwd_save/"),
    path('edit_adminpwd_save/',views.edit_adminpwd_save,name="edit_adminpwd_save/"),
    path('all_out/',adminviews.all_out,name="all_out/"),
    path('delete_student_save/<str:student_id>',adminviews.delete_student_save,name="delete_student_save/"),
]
