from rest_framework import serializers
from .models import Posts, Users

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['user_id', 'avatar_url', 'nickname', 'gender']

class PostsSerializer(serializers.ModelSerializer):
    usersId = serializers.IntegerField(source = 'Users.user_id')
    usersHeadUrl = serializers.URLField(source = 'Users.avatar_url')
    usersName = serializers.CharField(source = 'Users.nickname')
    usersGender = serializers.IntegerField(source = 'Users.gender')
    class Meta:
        model = Posts
        fields = ['usersId', 'usersHeadUrl', 'usersName', 'usersGender', 'post_id', 'post_desc', 'post_media_type', 'post_media_urls', 'post_like_num', 'post_share_num']
