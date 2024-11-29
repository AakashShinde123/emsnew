"""college_management_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path


from . import hod_views, staff_views,views

urlpatterns = [
    path("", views.login_page, name='login_page'),
    path("firebase-messaging-sw.js", views.showFirebaseJS, name='showFirebaseJS'),
    path("doLogin/", views.doLogin, name='user_login'),
    path("logout_user/", views.logout_user, name='user_logout'),
    path("admin/home/", hod_views.admin_home, name='admin_home'),
    path("staff/add", hod_views.add_staff, name='add_staff'),
    path("department/add", hod_views.add_department, name='add_department'),
   
    path("send_staff_notification/", hod_views.send_staff_notification,
         name='send_staff_notification'),
    path("admin_notify_staff", hod_views.admin_notify_staff,
         name='admin_notify_staff'),
    path("admin_view_profile", hod_views.admin_view_profile,
         name='admin_view_profile'),

    path('admin/delete-notification/<int:notification_id>/', hod_views.delete_notification, name='delete_notification'),

    path("check_email_availability", hod_views.check_email_availability,
         name="check_email_availability"),
    
    path("staff/view/complaint/", hod_views.staff_complaint_message,
         name="staff_complaint_message",),
    
    path("staff/view/leave/", hod_views.view_staff_leave, name="view_staff_leave",),
    
   
   

   
    path("staff/manage/", hod_views.manage_staff, name='manage_staff'),
    path("department/manage/", hod_views.manage_department, name='manage_department'),

    path("staff/edit/<int:staff_id>", hod_views.edit_staff, name='edit_staff'),
    path("staff/delete/<int:staff_id>",
         hod_views.delete_staff, name='delete_staff'),
    path("department/delete/<int:department_id>",
         hod_views.delete_department, name='delete_department'),
    path("department/edit/<int:department_id>",
         hod_views.edit_department, name='edit_department'),
    path('delete_complaint/', hod_views.delete_complaint, name='delete_complaint'),
    


    # Staff
    path("staff/home/", staff_views.staff_home, name='staff_home'),
    path("staff/apply/leave/", staff_views.staff_apply_leave,
         name='staff_apply_leave'),
    path("staff/complaint/", staff_views.staff_complaint, name='staff_complaint'),
    path("staff/view/profile/", staff_views.staff_view_profile,
         name='staff_view_profile'),
    path("staff/fcmtoken/", staff_views.staff_fcmtoken, name='staff_fcmtoken'),
    path("staff/view/notification/", staff_views.staff_view_notification,
         name="staff_view_notification"),
   
 


]