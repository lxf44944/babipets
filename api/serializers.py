
from rest_framework import serializers
from .models import Posts, Users


class PostsSerializer(serializers.ModelSerializer):
    # 通过外键user获取发帖用户相关信息
    UserId = serializers.ReadOnlyField(source='user.user_id')
    UserHeadUrl = serializers.ReadOnlyField(source='user.avatar_url')
    UserName = serializers.ReadOnlyField(source='user.nickname')
    UserGender = serializers.ReadOnlyField(source='user.gender')
    # 获取帖子相关信息
    PostId = serializers.ReadOnlyField(source='post_id')
    PostDesc = serializers.ReadOnlyField(source='post_desc')
    PostMediaType = serializers.ReadOnlyField(source='post_media_type')
    PostMediaUrls = serializers.JSONField(source='post_media_urls')
    PostLikeNum = serializers.ReadOnlyField(source='post_like_num')
    PostShareNum = serializers.ReadOnlyField(source='post_share_num')

    class Meta:
        model = Posts
        fields = ['UserId', 'UserHeadUrl', 'UserName', 'UserGender', 'PostId', 'PostDesc', 'PostMediaType',
                  'PostMediaUrls', 'PostLikeNum', 'PostShareNum']

class CreateSerializer(serializers.ModelSerializer):

    postDesc = serializers.CharField(source='post_desc')
    postMediaType = serializers.IntegerField(source='post_media_type')
    postMediaUrls = serializers.JSONField(source='post_media_urls')
    currentUserId = serializers.IntegerField(source ='user_id')
    userClient = serializers.IntegerField(source = 'user_client')

    class Meta:
        model = Posts
        fields = ['postDesc', 'postMediaType', 'postMediaUrls', 'currentUserId', 'userClient']

class UserSerializer(serializers.ModelSerializer):
    openId = serializers.CharField(source = 'openid')
    nickName = serializers.CharField(source = 'nickname')
    avatarUrl = serializers.CharField(source = 'avatar_url')
    gender = serializers.IntegerField()
    country = serializers.CharField()
    province = serializers.CharField()
    city = serializers.CharField()
    language = serializers.CharField()
    userClient = serializers.IntegerField(source = 'user_client')

    class Meta:
        model = Users
        fields = ['openId', 'nickName', 'avatarUrl', 'gender', 'country', 'province', 'city', 'language', 'userClient']

class EditUserSerializer(serializers.ModelSerializer):

    userDesc = serializers.CharField(source = 'user_desc')
    currentUserId = serializers.IntegerField(source = 'user_id')
    userClient = serializers.IntegerField(source = 'user_client')

    class Meta:
        model = Users
        fields = ['userDesc', 'currentUserId', 'userClient']
