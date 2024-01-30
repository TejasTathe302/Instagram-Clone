"""
URL configuration for instagramProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from instagramApp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home_page),
    path('registeration_page/', views.registeration_page),
    path('register_user/',views.register_user),
    path('login_page/',views.login_page),
    path('do_login/',views.do_login),
    path('log_out/',views.log_out),
    path('profile_page/',views.profile_page),
    path('edit_profile/',views.edit_profile),
    path('add_post/',views.add_post),
    path('final_post_save/',views.final_post_save),
    path('add_detail_of_post/',views.add_detail_of_post),
    path('save_edited_user/',views.save_edited_user),
    path('canclePost/',views.canclePost),
    path('view_profile_of_frind/',views.view_profile_of_frind),
    path('save_comment/',views.save_comment),
    path('add_like/',views.add_like),
    path('remove_like/',views.remove_like),
    path('mymodel/',views.mymodel),
    path('add_follow/',views.add_follow),
    path('remove_follow/',views.remove_follow), 
]
