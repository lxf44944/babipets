from rest_framework.generics import GenericAPIView
from chongbao.pagination import CustomPagination
from .serializers import PostsSerializer, CreateSerializer, UserSerializer, EditUserSerializer, LikeSerializer, ShareSerializer, UpdatePostSerializer, RewardSerializer, BalanceSerializer
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView, View



from .models import Post, User, Action, Balance
from rest_framework import permissions
from rest_framework.response import Response
from django.http import HttpResponseBadRequest
from django.db.models import Sum
from rest_framework.decorators import action
from .permissions import IsCurrentUser, OncePerDay

from rest_framework import permissions, status, viewsets
from rest_framework.permissions import AllowAny

from demo.sts_demo import getKey
import os



class List(GenericAPIView):
    serializer_class = PostsSerializer
    queryset = Post.objects.all()
    pagination_class = CustomPagination
    permission_classes = (permissions.AllowAny,)
    http_method_names = ['get', 'head']
    def get(self, request):
        def filter_queryset(queryset):
            return queryset.filter(deleted = 0)
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

    def get(self, request):
        queryset = Post.objects.filter(post_id = request.GET.get('postId'))
        #print(request.data.get('postId'))
        #queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many = True)

        data = serializer.data
        #data = request.GET.get('postId')

        payload = {
            'code': 200,
            'message': 'ok',
            'data':{
                'Item':data
            }
        }
        #payload['data']['item'] = request.data.get('postId')

        return Response(payload)

class add(APIView):
    def post(self, request):
        serializer = CreateSerializer(data = request.data)
        if serializer.is_valid():
            new = serializer.save()
            user = User.objects.filter(user_id = new.user)
            if user.posted == 0:
                user.update(posted, 1)
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
                        "UserDesc":newUser.user_desc,
                        "Posted":newUser.posted
                    }
                }
            }
            return Response(payload)
        return Response(serializer.errors)

class edit(APIView):
    def post(self, request):
        obj = User.objects.get(user_id=request.data['currentUserId'])
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
    queryset = Post.objects.all()
    pagination_class = CustomPagination
    permission_classes = (permissions.AllowAny,)
    http_method_names = ['get', 'head']
    def get(self, request):
        def filter_queryset(queryset):
            queryset = queryset.filter(deleted = 0)
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
        REDIRECT_URL = WEICHAT_AUTH['ROOT_URL'] + reverse('login:get_openid')
        auth_url = auth_url.format(appId = WEICHAT_AUTH['APPId'], redirect_url = quote(REDIRECT_URL))
        return redirect(auth_url)

def get_user_token(code):
    request_url = 'https://api.weixin.qq.com/sns/oauth2/access_token?' \
                      'appid={APPID}&secret={SECRET}&code={CODE}&grant_type=authorization_code'
    request_url = request_url.format(APPID = WEICHAT_AUTH['APPId'], SECRET = WEICHAT_AUTH['SECRET'], CODE = code)
    data = requests.get(request_url)
    return data.json()

class SilenceGetOpenId(View):
    def get(self, request, *args, **kwargs):
        code = request.GET.get('code', '')
        if not code:
            return HttpResponseBadRequest('请求错误')

        data = get_user_token(code).json()
        open_id = data.get('openid', '')
        access_token = data.get('access_token', '')



#V0.2.1 Starts here:
#Delete post API:
class Update(APIView):
    def post(self, request):
        obj = Post.objects.get(post_id=request.data['postId'])
        serializer = DeletePostSerializer(obj, data = request.data)
        if serializer.is_valid():
            editUser = serializer.save()
            #data = serializer.data.post_id
            payload = {
                "code": 200,
                "message": "ok",
            }
            return Response(payload)
        return Response(serializer.errors)

#return activity number for given user:
class Activity(GenericAPIView):
    def get(self, request):
        postNum = Post.objects.filter(user=request.data['userId']).count()
        commentNum = Action.objects.filter(user=request.data['userId'], comment=1).count()
        likeNum = Action.objects.filter(user=request.data['userId'], like=1).count()
        followNum = Followandinvite.objects.filter(follower_id=request.data['userId'], follow_relationship=1).count()
        usersPosts = Post.objects.filter(user=request.data['userId'])
        commentNum = Action.objects.filter(post=usersPosts.post_id, comment=1).count()

        activityNum = postNum + commentNum + likeNum + followNum

        payload = {
            "code": 200,
            "message": "ok",
            "activity": activityNum,
        }
        return Response(payload)

class LikeNumber(GenericAPIView):
    def get(self, request):
        usersPosts = Post.objects.filter(user=request.data['userId'])
        likeNum = Action.objects.filter(post=userPosts.post_id, like=1).count()

        payload = {
            "code": 200,
            "message": "ok",
            "like": likeNum,
        }
        return Response(payload)

class Reward(APIView):
    def post(self, request):
        serializer = RewardSerializer(data = request.data)
        if serializer.is_valid():
            newReward = serializer.save()
            #data = serializer.data.post_id
            payload = {
                "code": 200,
                "message": "ok",
            }
            return Response(payload)
        return Response(serializer.errors)

class CheckInViewSet(viewsets.GenericViewSet):
    queryset = User.objects.all()
    permission_classes = [AllowAny, ]

    @action(
        methods=['post'],
        detail=True,
        permission_classes=[permissions.IsAuthenticated, OncePerDay, IsCurrentUser]
    )
    def checkin(self, request, pk=None):
        user = self.get_queryset()

        random_amount = abs(random.gauss(10, 5)) #need to change this amount to one that we decide
        random_amount = math.ceil(random_amount)

        if random_amount == 0:
            random_amount += 1

        balance = Balance.objects.create(
            reward_type=0,
            coin_type=2,
            amount=random_amount,
            user=user
        )
        serializer = BalanceSerializer(balance)
        return Response(serializer.data, status=status.HTTP_201_CREATED) # post this change of output to shimo
