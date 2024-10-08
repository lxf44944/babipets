# Generated by Django 3.0.3 on 2020-10-01 20:14

from django.db import migrations, models
import django.db.models.deletion
import django_mysql.models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20200903_0618'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
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
                ('status', models.IntegerField(default=0)),
                ('deleted', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'Posts',
            },
        ),
        migrations.RenameModel(
            old_name='Actions',
            new_name='Action',
        ),
        migrations.RenameModel(
            old_name='Users',
            new_name='User',
        ),
        migrations.DeleteModel(
            name='Posts',
        ),
        migrations.AddField(
            model_name='post',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.User'),
        ),
        migrations.AlterField(
            model_name='action',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Post'),
        ),
    ]
