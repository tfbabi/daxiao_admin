import json

from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.authtoken.views import APIView,AuthTokenSerializer
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
# Create your views here.
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse,JsonResponse
##db cursor

from common import DbUtils
import time,datetime,re

def GetDbList(requests):
    employee = DbUtils.Model()
    author_name = requests.GET.get('author_name')
    if author_name:

        dbsql = "select * from author_say where author_name = '{0}' order by publish_time desc;".format(author_name)
        print(dbsql)
    else:
        dbsql = "select * from author_say order by publish_time desc;"
    apm_db_list=employee.fetchall(dbsql)
    apm_db_list={'data':apm_db_list}
    apm_db_list['code'] = 200
    return JsonResponse(apm_db_list)
def SyncNews(request):
    employee = DbUtils.Model()
    dbsql = "select * from sync_news where news_type='11' order by news_publish_time desc;"
    apm_db_list=employee.fetchall(dbsql)
    apm_db_list={'data':apm_db_list}
    apm_db_list['code'] = 200
    return JsonResponse(apm_db_list)
def HotNews(request):
    employee = DbUtils.Model()
    #dbsql = "SELECT  * from base_news  WHERE  news_type ='2' AND DATE_SUB(CURDATE(), INTERVAL 1 DAY) <= date(news_publish_time) order by news_publish_time desc;"
    dbsql = "SELECT  * from base_news  WHERE  news_type ='2' AND DATE_SUB(NOW(), INTERVAL 24 HOUR) <= date(news_publish_time) order by news_publish_time desc;"
    apm_db_list=employee.fetchall(dbsql)
    apm_db_list={'data':apm_db_list}
    apm_db_list['code'] = 200
    return JsonResponse(apm_db_list)
def FuPan(request):
    employee = DbUtils.Model()
    dbsql = "select * from base_news where news_type='3' order by news_publish_time desc;"
    apm_db_list=employee.fetchall(dbsql)
    apm_db_list={'data':apm_db_list}
    apm_db_list['code'] = 200
    return JsonResponse(apm_db_list)
def DavSay(request):
    employee = DbUtils.Model()
    dbsql = "select * from base_news where news_type='12' order by news_publish_time desc;"
    apm_db_list=employee.fetchall(dbsql)
    apm_db_list={'data':apm_db_list}
    apm_db_list['code'] = 200
    return JsonResponse(apm_db_list)

def GetAuthorName(request):
    employee = DbUtils.Model()
    dbsql = "SELECT author_name as value  from author_say GROUP BY author_name"
    apm_db_list=employee.fetchall(dbsql)
    value1=[]
    for li in apm_db_list:
        value1.append(li['value'])
    apm_db_list={'data':apm_db_list}
    apm_db_list['code'] = 200
    apm_db_list['value1'] = value1
    return JsonResponse(apm_db_list)

def GetArticleInfo(request,id):
    employee = DbUtils.Model()
    dbsql = "SELECT* from base_news where id = {0}".format(id)
    apm_db_list=employee.fetchall(dbsql)
    apm_db_list={'data':apm_db_list}
    apm_db_list['code'] = 200
    return JsonResponse(apm_db_list)