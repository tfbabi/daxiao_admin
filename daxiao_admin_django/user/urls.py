# -*- coding: utf-8 -*-
# @Time : 2023/7/2 9:48 AM
# @Author : mos
# @Email : tfbabi@163.com
# @File : urls.py

from django.conf.urls import url, include
from user import views


urlpatterns = [
    url('^user/register/$', views.Register.as_view(),name='register'),
    url('^user/login/$',views.Login.as_view(),name='login'),
    url('^user/logout/$',views.Logout.as_view(),name='logout'),
    url('^user/userinfo/$',views.userinfo.as_view(),name='userinfo'),
]