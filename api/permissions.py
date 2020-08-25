from django.utils import timezone
from rest_framework import permissions
from models import Balance

class OncePerDay(permissions.BasePermission):
    """
    one check in a day at most for each user
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        try:
            #try to find the latest checkin record, if none, means never did it before
            latest_record = request.user.record_set.latest('created_time') #need to confirm
        except Balance.DoesNotExist:
            return True

        today_start = timezone.now().replace(hour=0, minute=0, second=0)
        today_end = timezone.now(),replace(hour=23, minute=59, second=59)

        if today_start <= latest_record.created_time <= today_end:
            return False

        return True

class IsCurrentUser(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj == request.user
