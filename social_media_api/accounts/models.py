from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # Your custom fields go here

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='accounts_user_groups', # <-- Add this line
        blank=True,
        help_text=('The groups this user belongs to. A user will get all permissions '
                   'granted to each of their groups.'),
        related_query_name='user',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='accounts_user_permissions', # <-- Add this line
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='user',
    )