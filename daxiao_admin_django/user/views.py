
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
import time,datetime
from django.conf import global_settings


class BaseResponse(object):
    def __init__(self):
        self.code = 1000
        self.msg = ""
        self.data = None
        self.token = ""

    @property
    def dict(self):
        return self.__dict__


class Register(APIView):
    def post(self,request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        if User.objects.filter(username=username).exists():
            resp = {
                'status':False,
                'data':'用户名已被注册'
            }
        else:
            user = User.objects.create_user(username=username,password=password)
            token, created = Token.objects.get_or_create(user=user)
            resp = {
                'status':True,
                'token': token.key,
                'user_id': user.pk,
                'user_name': user.username,
            }
        return Response(resp)

# 用户登录
class Login(APIView):
    def post(self, request, *args, **kwargs):
        ret = BaseResponse()
        serializer = AuthTokenSerializer(data=request.data,context={'request': request})
        if serializer.is_valid():
            user = serializer.validated_data['user']
            # 每次用户登录时先删除Token再重新生成Token
            Token.objects.filter(user=user).delete()
            token, created = Token.objects.get_or_create(user=user)
            ret.msg = "登录成功！"
            ret.token = token.key
            ret.code = 200
            ret.data = {'user_name':user.username,'user_id':user.pk}

        else:
            # 登录失败时返回的内容
            ret.code = 403
            ret.msg = "登录失败！用户名或密码错！"
        return Response(ret.dict)




class userinfo(APIView):
    authentication_classes = [TokenAuthentication]
    #支持token认证
    # 只有登录才能访问
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        ret = BaseResponse()
        username=str(request.user)
        userdata=User.objects.filter(username=username).values()
        if userdata:
            ret.code=200
            ret.name=username
            #ret.avatar='../../assets/images/img.jpg'
            ret.avatar='http://localhost:8088/static/images/user/head.jpeg'
            ret.data=list(userdata)[0]

        else:
            # 登录失败时返回的内容
            ret.code = 403
            ret.msg = "登录失败！用户信息获取失败!"
        return Response(ret.dict)

class Logout(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request):
        ret =BaseResponse()
        try:
            # 退出时删除用户登录时生成的Token
            Token.objects.filter(user=request.user).delete()
            ret.msg = "注销成功！"
            ret.code = 200

        except Exception as e:
            ret.code = 1013
            ret.msg = str(e)
        return Response(ret.dict)


def index(request):
    if request.method=='GET':
        return HttpResponse("欢迎光临 大家后台!")
def api1(requests):
    return HttpResponse('this  is  api1!')

def api2(requests):
    return HttpResponse('this  is  api2')

def api3(requests):
    return HttpResponse('this  is  api3!')

def api4(requests):
    return HttpResponse('this  is  final_api!')
