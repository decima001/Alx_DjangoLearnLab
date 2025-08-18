# accounts/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models


def profile_upload_path(instance, filename):
    return f"profiles/user_{instance.id}/{filename}"


class User(AbstractUser):
    bio = models.TextField(blank=True, null=True)  # User biography
    profile_picture = models.ImageField(upload_to="profile_pics/", blank=True, null=True)  # Profile picture upload
    followers = models.ManyToManyField("self", symmetrical=False, related_name="followed_by", blank=True)  # Self-referential ManyToMany for following system
    following = models.ManyToManyField("self", symmetrical=False, related_name="follows", blank=True)

    def followers_count(self):
        return self.followers.count()

    def following_count(self):
        return self.following.count()

    def __str__(self):
        return self.username