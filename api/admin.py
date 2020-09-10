from django.contrib import admin
from .models import User, Post, Action, Review, Followandinvite, Reward, Balance
# Register your models here.
admin.site.register(Post)
admin.site.register(User)
admin.site.register(Action)
admin.site.register(Followandinvite)
admin.site.register(Review)
admin.site.register(Reward)
admin.site.register(Balance)
