
from rest_framework import serializers
from .models import Posts, Users, Actions, Followandinvite, Review, Reward, Balance
import datetime

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

class LikeSerializer(serializers.ModelSerializer):
    postId = serializers.IntegerField(source = 'post_id')
    activity_time = serializers.DateField(default = datetime.datetime.now)
    like = serializers.IntegerField(default = 1)
    share = serializers.IntegerField(default = 0)
    currentUserId = serializers.IntegerField(source = 'user_id')

    class Meta:
        model = Actions
        fields = ['postId', 'activity_time', 'like', 'share', 'currentUserId']

class ShareSerializer(serializers.ModelSerializer):
    postId = serializers.IntegerField(source = 'post_id')
    activity_time = serializers.DateField(default = datetime.datetime.now)
    like = serializers.IntegerField(default = 0)
    share = serializers.IntegerField(default = 1)
    currentUserId = serializers.IntegerField(source = 'user_id')

    class Meta:
        model = Actions
        fields = ['postId', 'activity_time', 'like', 'share', 'currentUserId']

class UpdatePostSerializer(serializers.ModelSerializer):
    status = serializers.IntegerField(source = 'status')

    class Meta:
        model = Posts
        fields = ['status']

class RewardSerializer(serializers.ModelSerializer):
    receiving_end = serializers.IntegerField(source = 'receiver')
    type_of_reward = serializers.IntegerField(source = 'type')
    reward_amount = serializers.IntegerField(source = 'amount')
    offering_end = serializers.IntegerField(source = 'offer_user_id')

    class Meta:
        model = Reward
        fields = ['receiving_end', 'type_of_reward', 'reward_amount', 'offering_end']

class BalanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Balance
        fields = (
            'reward_type',
            'coin_type',
            'amount',
            'user',
        )
        read_only_fields = (
            'reward_type',
            'coin_type',
            'amount',
            'user',
        )
