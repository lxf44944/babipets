from rest_framework.generics import GenericAPIView
from project_name.pagination import CustomPagination
from .serializers import PostsSerializer
from .models import Posts

class PostList(GenericAPIView):
    serializer_class = PostsSerializer
    queryset = Posts.objects.all()
    pagination_class = CustomPagination
    def list(self, request):
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
        return Response(data) # return Response(payload) ??? 
