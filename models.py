# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class TActivity(models.Model):
    post = models.OneToOneField('TPost', models.DO_NOTHING, primary_key=True)
    activity_time = models.DateTimeField(blank=True, null=True)
    activity_type = models.IntegerField(blank=True, null=True)
    user = models.ForeignKey('TUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 't_activity'
        unique_together = (('post', 'user'),)


class TPost(models.Model):
    post_id = models.BigIntegerField(primary_key=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    user_id = models.BigIntegerField(blank=True, null=True)
    user_client = models.IntegerField(blank=True, null=True)
    post_desc = models.CharField(max_length=200, blank=True, null=True)
    post_media_type = models.IntegerField(blank=True, null=True)
    post_media_urls = models.TextField(blank=True, null=True)  # This field type is a guess.
    post_like_num = models.IntegerField(blank=True, null=True)
    post_share_num = models.IntegerField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_post'


class TUser(models.Model):
    user_id = models.BigIntegerField(primary_key=True)
    openid = models.BigIntegerField(blank=True, null=True)
    nickname = models.CharField(max_length=20, blank=True, null=True)
    avatar_url = models.CharField(max_length=60, blank=True, null=True)
    gender = models.IntegerField(blank=True, null=True)
    user_client = models.IntegerField(blank=True, null=True)
    user_desc = models.CharField(max_length=200, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    country = models.CharField(max_length=30, blank=True, null=True)
    province = models.CharField(max_length=30, blank=True, null=True)
    city = models.CharField(max_length=30, blank=True, null=True)
    language = models.CharField(max_length=30, blank=True, null=True)
    deleted_user = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_user'
