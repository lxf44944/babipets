from rest_framework.generics import GenericAPIView
from chongbao.pagination import CustomPagination
from .serializers import PostsSerializer, CreateSerializer, UserSerializer, EditUserSerializer, LikeSerializer, ShareSerializer
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView, View



from .models import Posts, Users, Actions
from rest_framework import permissions
from rest_framework.response import Response
from django.http import HttpResponseBadRequest

from demo.sts_demo import getKey
import os

class List(GenericAPIView):
    serializer_class = PostsSerializer
    queryset = Posts.objects.all()
    pagination_class = CustomPagination
    permission_classes = (permissions.AllowAny,)
    http_method_names = ['get', 'head']
    def get(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            result = self.get_paginated_response(serializer.data)
            data = result.data # pagination data
        else:
            serializer = self.get_serializer(queryset, many=True)
            data = serializer.data

        payload = {
            'code': '200',
            'message': 'ok',
            'data': data
        }
        return Response(payload) # return Response(payload) ???

class Info(GenericAPIView):
    serializer_class = PostsSerializer
    queryset = Posts.objects.all()
    def get(self, request):
        def filter_queryset(queryset):
            return queryset.filter(pk = request.query_params.get('postId'))
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many = True)
        data = serializer.data

        payload = {
            'code': 200,
            'message': 'ok',
            'data':{
                #'Item':data
            }
        }
        payload['data']['item'] = data

        return Response(payload)

class add(APIView):
    def post(self, request):
        serializer = CreateSerializer(data = request.data)
        if serializer.is_valid():
            new = serializer.save()
            #data = serializer.data.post_id
            payload = {
                "code": 200,
                "message": "ok",
                "data":{
                    "Item":{
                        "PostId":new.post_id
                    }
                }
            }
            return Response(payload)
        return Response(serializer.errors)

class secret(APIView):
    def post(self, request):
        os.environ['COS_SECRET_ID'] = 'AKIDamh93ecLU98rKsaYTBZonSqywaS3323i'
        os.environ['COS_SECRET_KEY'] = 'gCdvtCF3ZouyeHNK1FrEMFqZ36twjESO'
        data = getKey()
        payload = {
            "code": 200,
            "message": "ok",
            "data":{
                "Item":{
                    "tmpSecretId":data['credentials']['tmpSecretId'],
                    "tmpSecretKey":data['credentials']['tmpSecretKey'],
                    "sessionToken":data['credentials']['sessionToken']
                }
            }
        }
        return Response(payload)

class login(APIView):
    def post(self, request):
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid():
            newUser = serializer.save()
            #data = serializer.data.post_id
            payload = {
                "code": 200,
                "message": "ok",
                "data":{
                    "Item":{
                        "UserId":newUser.user_id,
                        "UserHeadUrl":newUser.avatar_url,
                        "UserName":newUser.nickname,
                        "UserGender":newUser.gender,
                        "UserDesc":newUser.user_desc
                    }
                }
            }
            return Response(payload)
        return Response(serializer.errors)

class edit(APIView):
    def post(self, request):
        obj = Users.objects.get(user_id=request.data['currentUserId'])
        serializer = EditUserSerializer(obj, data = request.data)
        if serializer.is_valid():
            editUser = serializer.save()
            #data = serializer.data.post_id
            payload = {
                "code": 200,
                "message": "ok",
            }
            return Response(payload)
        return Response(serializer.errors)

class history(GenericAPIView):
    serializer_class = PostsSerializer
    queryset = Posts.objects.all()
    pagination_class = CustomPagination
    permission_classes = (permissions.AllowAny,)
    http_method_names = ['get', 'head']
    def get(self, request):
        def filter_queryset(queryset):
            return queryset.filter(user = request.query_params.get('userId'))
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            result = self.get_paginated_response(serializer.data)
            data = result.data # pagination data
        else:
            serializer = self.get_serializer(queryset, many=True)
            data = serializer.data

        payload = {
            'code': '200',
            'message': 'ok',
            'data': data
        }
        return Response(payload) # return Response(payload) ???

class like(APIView):
    def post(self, request):
        serializer = LikeSerializer(data = request.data)
        if serializer.is_valid():
            newLike = serializer.save()
            #data = serializer.data.post_id
            payload = {
                "code": 200,
                "message": "ok",
            }
            return Response(payload)
        return Response(serializer.errors)

class share(APIView):
    def post(self, request):
        serializer = ShareSerializer(data = request.data)
        if serializer.is_valid():
            newLike = serializer.save()
            #data = serializer.data.post_id
            payload = {
                "code": 200,
                "message": "ok",
            }
            return Response(payload)
        return Response(serializer.errors)

class DefaultAutoView(View):
    def get(self, request, *args, **kwargs):
        auth_url = 'https://open.weixin.qq.com/connect/oauth2/authorize?appid={APPID}&redirect_uri={redirect_url}&response_type=code&scope=snsapi_base&state=123#wechat_redirect'
        REDIRECT_URL = request.query_params.get('ROOT_URL') + reverse('login:get_openid')
        auth_url = auth_url.format(appId = request.query_params.get('APPID'), redirect_url = quote(REDIRECT_URL))
        return redirect(auth_url)

def get_user_token(code, appId, secret):
    request_url = 'https://api.weixin.qq.com/sns/oauth2/access_token?' \
                      'appid={APPID}&secret={SECRET}&code={CODE}&grant_type=authorization_code'
    request_url = request_url.format(APPID = appId, SECRET = secret, CODE = code)
    data = requests.get(request_url)
    return data.json()

class SilenceGetOpenId(View):
    def get(self, request, *args, **kwargs):
        code = request.GET.get('code', '')
        appId = request.query_params.get('APPID')
        secret = request.query_params.get('SECRET')
        if not code:
            return HttpResponseBadRequest('请求错误')

        data = get_user_token(code, ).json()
        open_id = data.get('openid', '')
        access_token = data.get('access_token', '')
