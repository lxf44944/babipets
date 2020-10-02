from django.conf.urls import include, url
from rest_framework.urlpatterns import format_suffix_patterns
from api import views
from api.views import CheckInViewSet
from django.urls import path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', CheckInViewSet) #need to confirm

urlpatterns = [
    path('home/list.json', views.List.as_view(), name = 'list'),
    path('home/info.json', views.Info.as_view(), name = 'info'),
    path('post/update.json', views.Update.as_view(), name = 'update'), # update a selected post by changing status feature from 0 to 1
    path('user/activity.json', views.Activity.as_view(), name = 'activity'),
    path('user/likeNumber.json', views.LikeNumber.as_view(), name = 'like'),
    path('post/add.json', views.add.as_view(), name = 'add'),
    path('post/secret.json', views.secret.as_view(), name = 'secret'),
    path('user/login.json', views.login.as_view(), name = 'login'),
    path('user/edit.json', views.edit.as_view(), name = 'edit'),
    path('user/history.json', views.history.as_view(), name = 'history'),
    path('post/like.json', views.like.as_view(), name = 'like'),
    path('post/share.json', views.share.as_view(), name = 'share'),
    path('user/reward.json', views.Reward.as_view(), name = 'reward'),
    url(r'user/checkIn/', include(router.urls)),
    path('get/openid/', views.SilenceGetOpenId.as_view(), name = 'get_openid'),
]
