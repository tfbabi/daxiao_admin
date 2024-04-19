# -*- coding: utf-8 -*-
# @Time : 2023/11/5 9:42 AM
# @Author : mos
# @Email : tfbabi@163.com
# @File : urls.py


from django.conf.urls import url, include
from user import views
from basic_dashboard import views


urlpatterns = [
    url('^basic/pan/$',views.Get_Pankou_Data,name='概念'),
    url('^basic/index$',views.Get_Basic_Data,name='大盘盘口'),
    url('^basic/pankouyidong',views.Get_Pankou_Yidong,name='盘口异动'),
    url('^basic/zthistory',views.Get_Zt_History,name='涨跌停历史')

]