from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from api import views
from django.urls import path

urlpatterns = [
    path('home/list.json', views.List.as_view(), name = 'list'),
    path('home/info.json', views.Info.as_view(), name = 'info'),
    path('post/add.json', views.add.as_view(), name = 'add'),
    path('post/secret.json', views.secret.as_view(), name = 'secret'),

    #path('browsingPageAPI/<int:pk>/', views.Browse.as_view()),
]
