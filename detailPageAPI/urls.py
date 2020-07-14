from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from detailPageAPI import views
from django.urls import path

urlpatterns = [
    path('home/info.json', views.PostList.as_view(), name = 'detail-page'),
]
