#from django.shortcuts import render
# Create your views here.
from rest_framework.generics import ListAPIView
from .serializers import PostsSerializer
from rest_framework.decorators import api_view
from .models import Posts
from rest_framework.response import Response


class PostList(ListAPIView):
    response = {
        'code': 200,
        'message': 'ok',
        'data':{
            'Item':{}
        }
    }
    serializer = PostsSerializer( many = True)
    response['data']['Item'] = serializer.data #auto recognized as result?
    #def list(self, request, *args, **kwargs):
    def get_queryset(self):
        return Posts.objects.filter(post_id = self.request.postId)
    #return Response(response.data)
