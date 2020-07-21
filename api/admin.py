from django.contrib import admin
from .models import Users, Posts, Actions
# Register your models here.
admin.site.register(Posts)
admin.site.register(Users)
admin.site.register(Actions)
