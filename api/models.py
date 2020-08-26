# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.conf import settings
from django_mysql.models import JSONField

class Users(models.Model):
    user_id = models.BigAutoField(primary_key=True)
    openid = models.CharField(max_length=200, blank=True, null=True)
    nickname = models.CharField(max_length=20, blank=True, null=True)
    avatar_url = models.CharField(max_length=200,blank=True, null=True)
    gender = models.IntegerField(blank=True, null=True)
    user_client = models.IntegerField(blank=True, null=True)
    user_desc = models.CharField(max_length=200, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    country = models.CharField(max_length=30, blank=True, null=True)
    province = models.CharField(max_length=30, blank=True, null=True)
    city = models.CharField(max_length=30, blank=True, null=True)
    language = models.CharField(max_length=30, blank=True, null=True)
    deleted_user = models.IntegerField(default = 0) #make this change in mysql or do not pull data from db directly
    posted = models.IntegerField(default = 0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Users'


class Posts(models.Model):
    post_id = models.BigAutoField(primary_key=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey(Users, on_delete = models.CASCADE)
    user_client = models.IntegerField(blank=True, null=True)
    post_desc = models.CharField(max_length=200, blank=True, null=True)
    post_media_type = models.IntegerField(blank=True, null=True)
    post_media_urls = JSONField(blank=True, null=True)  # This field type is a guess.
    post_like_num = models.IntegerField(blank=True, null=True)
    post_share_num = models.IntegerField(blank=True, null=True)
    deleted = models.IntegerField(default = 0) #make this change in mysql or do not pull data from db directly

    class Meta:
        managed = False
        db_table = 'Posts'

class Actions(models.Model):
    action_id = models.BigAutoField(primary_key=True)
    post = models.ForeignKey(Posts, on_delete = models.CASCADE)
    activity_time = models.DateTimeField(blank=True, null=True)
    like = models.IntegerField(blank=True, null=True)
    share = models.IntegerField(blank=True, null=True)
    user = models.ForeignKey(Users, on_delete = models.CASCADE)
    comment = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Actions'


class Followandinvite(models.Model):
    follow_id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField()
    follower_id = models.BigIntegerField()
    follow_relationship = models.IntegerField(blank=True, null=True)
    invite_relationship = models.IntegerField(blank=True, null=True)
    #test_field = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'followAndInvite'

class Review(models.Model):
    review = models.OneToOneField(Actions, on_delete = models.CASCADE, primary_key=True)
    content = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'review'

class Reward(models.Model):
    reward_id = models.BigAutoField(primary_key=True)
    receiver = models.BigIntegerField()
    type = models.IntegerField()
    amount = models.IntegerField()
    offer_user_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = "reward"

class Balance(models.Model):
    REWARD_TYPE = (
        (0, 'check_in_reward'),
    )

    COIN_TYPE = (
        (0, 'gold'),
        (1, 'silver'),
        (2, 'bronze'),
    )

    created_time = models.DateTimeField("time_created", auto_now_add = True)
    reward_type = models.IntegerField("type_of_reward", choices = REWARD_TYPE)
    coin_type = models.IntegerField("type_of_coins", choices = COIN_TYPE)
    amount = models.PositiveIntegerField("amount_of_reward")
    user = models.ForeignKey(Users, on_delete = models.CASCADE, verbose_name = "user") 

    class Meta:
        verbose_name = "reward_record"
        verbose_name_plural = "reward_record"

    def __str__(self):
        return '%s:%s:%s -> %s' % (self.reward_type, self.coin_type, self.amount, self.user)
