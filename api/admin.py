from django.contrib import admin
from .models import Users, Posts, Actions, Review, Followandinvite
# Register your models here.
admin.site.register(Posts)
admin.site.register(Users)
admin.site.register(Actions)
admin.site.register(Followandinvite)
admin.site.register(Review)
