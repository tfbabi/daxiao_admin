# -*- coding: utf-8 -*-
# @Time : 2021/11/19 22:22
# @File : xueqiu_news
import re
from DbUtils import Model
import requests
import json
import time
from common import wx_send
from fake_useragent import UserAgent

employee = Model()
def Get_New_data(url,newsurl,headers):
    #忽略移除认证后控制台总是抛出警告
    requests.packages.urllib3.disable_warnings()
    req=requests.session()
    req.get(url,headers=headers,timeout=(5,10))
    data=req.get(newsurl,headers=headers,timeout=(5,10)).json()['items'][0]
    return data
#for line in data['items']:
#    print(time.strftime('%Y-%m-%d %H:%S',time.localtime(line['created_at']/1000)),line['text'],line['target'])



url='https://xueqiu.com/?category=livenews'
newsurl="https://xueqiu.com/statuses/livenews/list.json?since_id=-1&max_id=-1&count=-1"

ua = UserAgent(verify_ssl=False)
while True:
    headers = {
        'User-Agent': ua.random,
        'Host': 'xueqiu.com'
    }
    datanews = Get_New_data(url, newsurl, headers)
    last_time=datanews['created_at']
    #print(headers,last_time)
    #print(datanews)
    #print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(last_time/1000)))
    time.sleep(30)
    #print(Get_New_data(url,newsurl,headers)['created_at'])
    if Get_New_data(url,newsurl,headers)['created_at']==last_time:
        print("暂无新闻推送")
        continue
    else:
        news = Get_New_data(url, newsurl, headers)
        content = news['text']
        if re.findall('【',content):
            title=content.strip('【').split('】')[0]
            content=content.strip('【').split('】')[1]
        else:
            title='雪球网消息'
            content=content
        targeturl = news['target']
        ctime = time.strftime('%Y-%m-%d %H:%M', time.localtime(news['created_at']/1000))
        #msg = ctime +'\n' +content+ targeturl
        #wx=wx_send.WeChat(CORPSECRET='',AGENTID='1000002')
        #wx=wx_send.WeChat(CORPSECRET='',AGENTID='1000002')
        #wx.send_text_card(title=title,date=ctime,content=content,url=targeturl)
        sql="insert into xueqiu_news (title,content,url,ctime) values ('{0}','{1}','{2}','{3}')".format(str(title),str(content),str(targeturl),str(ctime))
        employee.change(sql)
        print(ctime,"成功推送一条新闻")

