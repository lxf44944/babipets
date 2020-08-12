from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from api import views
from django.urls import path

urlpatterns = [
    path('home/list.json', views.List.as_view(), name = 'list'),
    path('home/info.json', views.Info.as_view(), name = 'info'),
    path('home/delete.json', views.Delete.as_view(), name = 'delete'), # delete a selected post by changing deleted feature from 0 to 1
    path('post/add.json', views.add.as_view(), name = 'add'),
    path('post/secret.json', views.secret.as_view(), name = 'secret'),
    path('user/login.json', views.login.as_view(), name = 'login'),
    path('user/edit.json', views.edit.as_view(), name = 'edit'),
    path('user/history.json', views.history.as_view(), name = 'history'),
    path('post/like.json', views.like.as_view(), name = 'like'),
    path('post/share.json', views.share.as_view(), name = 'share'),
    path('get/openid/', views.SilenceGetOpenId.as_view(), name = 'get_openid'),

]
