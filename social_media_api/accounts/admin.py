from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User

# Add the following lines to define the counts

class UserAdmin(BaseUserAdmin):
    # This will be your list_display tuple, make sure it matches your file
    list_display = (
        'username',
        'email',
        'is_staff',
        'followers_count',  # Your referenced field
        'following_count',  # Your referenced field
    )

    # Define the methods to get the counts
    def followers_count(self, obj):
        return obj.followers.count()

    def following_count(self, obj):
        return obj.following.count()

admin.site.register(User, UserAdmin)