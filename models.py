# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Actions(models.Model):
    action_id = models.BigAutoField(primary_key=True)
    post = models.ForeignKey('Posts', models.DO_NOTHING)
    activity_time = models.DateTimeField(blank=True, null=True)
    like = models.IntegerField(blank=True, null=True)
    share = models.IntegerField(blank=True, null=True)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    review = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'actions'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Followandinvite(models.Model):
    follow_id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField()
    follower_id = models.BigIntegerField()
    follow_relationship = models.IntegerField(blank=True, null=True)
    invite_relationship = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'followAndInvite'


class Posts(models.Model):
    post_id = models.BigAutoField(primary_key=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    user_client = models.IntegerField(blank=True, null=True)
    post_desc = models.CharField(max_length=200, blank=True, null=True)
    post_media_type = models.IntegerField(blank=True, null=True)
    post_media_urls = models.TextField(blank=True, null=True)  # This field type is a guess.
    post_like_num = models.IntegerField(blank=True, null=True)
    post_share_num = models.IntegerField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'posts'


class Review(models.Model):
    review = models.OneToOneField(Actions, models.DO_NOTHING, primary_key=True)
    content = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'review'


class Users(models.Model):
    user_id = models.BigAutoField(primary_key=True)
    openid = models.CharField(max_length=200, blank=True, null=True)
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
    posted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'
