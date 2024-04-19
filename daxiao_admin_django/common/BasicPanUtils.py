# -*- coding: utf-8 -*-
# @Time : 2023/10/29 1:05 PM
# @Author : mos
# @Email : tfbabi@163.com
# @File : basic_panmian.py


import json
import time
from fake_useragent import UserAgent
import requests
from common.DbUtils import Model

class Basic():
    def __init__(self):
        self.url3='https://x-quote.cls.cn/quote/index/home?app=CailianpressWeb&os=web&sv=7.7.5&sign=bf0f367462d8cd70917ba5eab3853bce'
        self.ua = UserAgent()
        self.url='https://x-quote.cls.cn/web_quote/plate/hot_plate?app=CailianpressWeb&os=web&rever=1&sv=7.7.5&type=industry,concept,area&way=change&sign=db0c36ccbeedc38b0abf5b73e9b4ce21'
        self.now=int(time.strftime('%H%M'))
        self.headers={
            'User-Agent':self.ua.random,
            'Referer':'https://www.cls.cn/',
            'Host':'x-quote.cls.cn',
            'Origin':'https://www.cls.cn'
        }
    def Get_pankou_dict(self,website):
        requests.packages.urllib3.disable_warnings()
        response=requests.get(website,headers=self.headers,timeout=(5,10))
        data=response.json()['data']
        return data
    def Get_pankou_data(self):
        data=self.Get_pankou_dict(self.url)
        return data
    def Get_basic(self,type):
        data = self.Get_pankou_dict(self.url3)
        if type == 'index':
            return data['index_quote']
        elif type == 'up_down':
            return data['up_down_dis']
        elif type == 'listed_today':
            return data['listed_today']
        elif type == 'purchase_today':
            return data['purchase_today']
        elif type == 'zt_his':
            return self.Get_Zt_History()[0]
        elif type == 'zt_his_all':
            return self.Get_Zt_History()
    def Get_Zt_History(self):
        ua = UserAgent()
        url = 'https://gateway.jrj.com/quot-dc/zdt/market_history'
        headers = {
            'user-agent': ua.random,
            'Rerfer': 'https://summary.jrj.com.cn/',
            'authority': 'gateway.jrj.com',
            'Content-Type': 'application/json'
        }
        playload = json.dumps({})
        requests.packages.urllib3.disable_warnings()
        response = requests.post(url, headers=headers, data=playload, timeout=(5, 10))
        data = response.json()
        list = data['data']['list']
        for li in list:
            li['marketAmount']=round(li['marketAmount'] / 100000000, 2)
        return list
if __name__== '__main__':
    ba=Basic()
    print(ba.Get_Zt_History())