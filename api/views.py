from rest_framework.generics import GenericAPIView
from chongbao.pagination import CustomPagination
from .serializers import PostsSerializer, CreateSerializer
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView



from .models import Posts
from rest_framework import permissions
from rest_framework.response import Response

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
