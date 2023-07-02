# -*- coding: utf-8 -*-
# @Time : 2023/7/2 9:42 AM
# @Author : mos
# @Email : tfbabi@163.com
# @File : urls.py

from django.conf.urls import url, include
from user import views
from taoguba import views


urlpatterns = [
    url('^table/list/$',views.GetDbList,name='大v评论'),
    url('^table/sync_news/$',views.SyncNews,name='实时新闻'),
    url('^table/hot_news/$',views.HotNews,name='热门新闻'),
    url('^table/fupan/$',views.FuPan,name='复盘'),
    url('^table/davsay/$',views.DavSay,name='大v说'),
]