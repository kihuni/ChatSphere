# apps/users/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    
    bio = models.TextField(
        max_length=500, 
        blank=True, 
        help_text='User\'s personal description'
    )
    avatar = models.ImageField(
        upload_to='avatars/', 
        null=True, 
        blank=True
    )

    # Contextual Information
    location = models.CharField(max_length=100, blank=True)
    gender = models.CharField(
        max_length=1, 
        choices=[
            ('M', 'Male'), 
            ('F', 'Female'), 
            ('O', 'Other'), 
            ('N', 'Prefer Not to Say')
        ], 
        blank=True
    )

    # Platform Engagement Metrics
    joined_rooms_count = models.PositiveIntegerField(default=0)
    messages_sent = models.PositiveIntegerField(default=0)

    # Online Presence Tracking
    is_online = models.BooleanField(default=False)
    last_seen = models.DateTimeField(null=True, blank=True)