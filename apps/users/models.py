from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    """
    Custom user model for CollabSphere platform
    """
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    status = models.CharField(max_length=100, blank=True)
    last_seen = models.DateTimeField(auto_now=True)
    is_online = models.BooleanField(default=False)
    
    class Meta:
        db_table = 'auth_user'
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        return self.username
