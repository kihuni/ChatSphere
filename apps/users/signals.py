from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.utils import timezone
from .models import User

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """
    Signal to handle additional setup when a new user is created
    """
    if created:
        # Set default avatar if none provided
        if not instance.avatar:
            # You would implement default avatar logic here
            pass
        
        # Set initial status
        instance.status = "Available"
        instance.save()

@receiver(pre_save, sender=User)
def update_last_seen(sender, instance, **kwargs):
    """
    Update last_seen timestamp when user status changes
    """
    if instance.pk:  # Only for existing users
        try:
            previous = User.objects.get(pk=instance.pk)
            if previous.is_online != instance.is_online:
                instance.last_seen = timezone.now()
        except User.DoesNotExist:
            pass

# Create signal for user login
@receiver(post_save, sender=User)
def user_login_handler(sender, instance, **kwargs):
    """
    Handle user login status updates
    """
    if instance.is_online:
        # Could implement additional login handling here
        # For example, notify other users or update presence
        pass

# Create signal for user logout
@receiver(pre_save, sender=User)
def user_logout_handler(sender, instance, **kwargs):
    """
    Handle user logout status updates
    """
    if instance.pk:
        try:
            previous = User.objects.get(pk=instance.pk)
            if previous.is_online and not instance.is_online:
                # Could implement additional logout handling here
                # For example, cleanup sessions or notify others
                pass
        except User.DoesNotExist:
            pass

# You might also want to create a clean-up signal for old sessions
@receiver(post_save, sender=User)
def cleanup_old_sessions(sender, instance, **kwargs):
    """
    Clean up old sessions when user logs out
    """
    from django.contrib.sessions.models import Session
    if not instance.is_online:
        # Delete any existing sessions for this user
        Session.objects.filter(
            expire_date__lt=timezone.now()
        ).delete()