# Generated by Django 3.0.3 on 2020-08-28 05:36

from django.db import migrations, models
import django.db.models.deletion
import django_mysql.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actions',
            fields=[
                ('action_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('activity_time', models.DateTimeField(blank=True, null=True)),
                ('like', models.IntegerField(blank=True, null=True)),
                ('share', models.IntegerField(blank=True, null=True)),
                ('comment', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'Actions',
            },
        ),
        migrations.CreateModel(
            name='Followandinvite',
            fields=[
                ('follow_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('user_id', models.BigIntegerField(max_length=20)),
                ('follower_id', models.BigIntegerField(max_length=20)),
                ('follow_relationship', models.IntegerField(blank=True, null=True)),
                ('invite_relationship', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'followAndInvite',
            },
        ),
        migrations.CreateModel(
            name='Reward',
            fields=[
                ('reward_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('receiver', models.BigIntegerField(max_length=20)),
                ('type', models.IntegerField()),
                ('amount', models.IntegerField()),
                ('offer_user_id', models.BigIntegerField(max_length=20)),
            ],
            options={
                'db_table': 'reward',
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('user_id', models.BigAutoField(max_length=20, primary_key=True, serialize=False)),
                ('openid', models.CharField(blank=True, max_length=200, null=True)),
                ('nickname', models.CharField(blank=True, max_length=20, null=True)),
                ('avatar_url', models.CharField(blank=True, max_length=60, null=True)),
                ('gender', models.IntegerField(blank=True, max_length=10, null=True)),
                ('user_client', models.IntegerField(blank=True, max_length=10, null=True)),
                ('user_desc', models.CharField(blank=True, max_length=200, null=True)),
                ('create_time', models.DateTimeField(blank=True, null=True)),
                ('update_time', models.DateTimeField(blank=True, null=True)),
                ('country', models.CharField(blank=True, max_length=30, null=True)),
                ('province', models.CharField(blank=True, max_length=30, null=True)),
                ('city', models.CharField(blank=True, max_length=30, null=True)),
                ('language', models.CharField(blank=True, max_length=30, null=True)),
                ('deleted_user', models.IntegerField(default=0)),
                ('posted', models.IntegerField(blank=True, default=0, null=True)),
            ],
            options={
                'db_table': 'Users',
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('review', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='api.Actions')),
                ('content', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'review',
            },
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('post_id', models.BigAutoField(max_length=20, primary_key=True, serialize=False)),
                ('create_time', models.DateTimeField(blank=True, null=True)),
                ('update_time', models.DateTimeField(blank=True, null=True)),
                ('user_client', models.IntegerField(blank=True, null=True)),
                ('post_desc', models.CharField(blank=True, max_length=200, null=True)),
                ('post_media_type', models.IntegerField(blank=True, null=True)),
                ('post_media_urls', django_mysql.models.JSONField(blank=True, default=dict, null=True)),
                ('post_like_num', models.IntegerField(blank=True, null=True)),
                ('post_share_num', models.IntegerField(blank=True, null=True)),
                ('deleted', models.IntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Users')),
            ],
            options={
                'db_table': 'Posts',
            },
        ),
        migrations.CreateModel(
            name='Balance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='time_created')),
                ('reward_type', models.IntegerField(choices=[(0, 'check_in_reward')], verbose_name='type_of_reward')),
                ('coin_type', models.IntegerField(choices=[(0, 'gold'), (1, 'silver'), (2, 'bronze')], verbose_name='type_of_coins')),
                ('amount', models.PositiveIntegerField(verbose_name='amount_of_reward')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Users', verbose_name='user')),
            ],
            options={
                'verbose_name': 'reward_record',
                'verbose_name_plural': 'reward_record',
            },
        ),
        migrations.AddField(
            model_name='actions',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Posts'),
        ),
        migrations.AddField(
            model_name='actions',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Users'),
        ),
    ]
