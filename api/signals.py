from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import ProfileModel


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, *args, **kwargs):
    print('signal profile', instance.username, 'created', created)
    if created:
        profile = ProfileModel.objects.create(
            user_id=instance, username=instance.username)
        profile.save()
