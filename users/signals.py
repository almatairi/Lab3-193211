from django.db.models.signals import post_save , post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User

from .models import Profile

@receiver(post_save , sender=User)
def createProfile(sender , instance , created , **kwargs):
    if created:
        user = instance
        user = Profile.objects.create(
            user = user,
            username = user.username,
            email = user.email,
            name = user.first_name,
        )

    else:
        pass

@receiver(post_delete , sender=Profile)
def deleteUser(sender , instance , **kwargs):
    user = instance.user
    user.delete()
