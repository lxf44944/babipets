#from django.shortcuts import render
# Create your views here.
from rest_framework.generics import ListAPIView
from .serializers import PostsSerializer
from rest_framework.decorators import api_view
from .models import Posts
from rest_framework.response import Response


class PostList(ListAPIView):
    def list(self, request, *args, **kwargs):
        queryset = Posts.objects.all()
        def get_queryset(self, game_pk):
            return self.objects.filter(post_id = self.request.query_params.get('postId'))

        response = {
            'code': 200,
            'message': 'ok',
            'data':{
                'Item':{}
            }
        }
        serializer = PostsSerializer(queryset, many = True)
        response['data']['Item'] = serializer.data
        return Response(serializer.data)
