#from django.shortcuts import render
# Create your views here.
from rest_framework.generics import ListAPIView
from .serializers import PostsSerializer
from .models import Posts

class PostList(ListAPIView):
    def list(self, request, *args, **kwargs):
        queryset = Posts.objects.filter(post_id = self.request.query_params.get('postId'))
        response = {
            'code': 200,
            'message': 'ok',
            'data':{
                'Item':{}
            }
        }
        serializer = PostsSerializer(queryset, many = False)
        response['data']['Item'] = serializer.data
        return Response(response)
