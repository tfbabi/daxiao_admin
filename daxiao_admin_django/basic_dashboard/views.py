from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
# Create your views here.

from common import DbUtils
import time,datetime,re
from common import BasicPanUtils

ba= BasicPanUtils.Basic()

def Get_Pankou_Data(request):
    if request.method == 'GET':
        data=ba.Get_pankou_data()
        apm_db_list = {'data': data}
        apm_db_list['code'] = 200
        return JsonResponse(apm_db_list)
def Get_Basic_Data(request):
    if request.method == 'GET':
        type = request.GET.get('type')
        data=ba.Get_basic(type)
        apm_db_list = {'data': data}
        apm_db_list['code'] = 200
        return JsonResponse(apm_db_list)
def Get_Pankou_Yidong(request):
    if request.method == 'GET':
        today = time.strftime("%Y-%m-%d", time.localtime(time.time()))
        employee = DbUtils.Model()
        dbsql = "select * from pankou WHERE create_time like '{0}%' order by create_time ;".format(today)
        apm_db_list = employee.fetchall(dbsql)
        apm_db_list = {'data': apm_db_list}
        apm_db_list['code'] = 200
        return JsonResponse(apm_db_list)
def Get_Zt_History(request):
    if request.method == 'GET':
        data=ba.Get_Zt_History()
        apm_db_list = {'data': data}
        apm_db_list['code'] = 200
        return JsonResponse(apm_db_list)