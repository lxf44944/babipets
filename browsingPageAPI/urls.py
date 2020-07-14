from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from browsingPageAPI import views
from django.urls import path

urlpatterns = [
    path('home/list.json', views.Browse.as_view(), name = 'browse-page'),
    #path('browsingPageAPI/<int:pk>/', views.Browse.as_view()),
]
