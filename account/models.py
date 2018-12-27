from django.db import models
from django.contrib.auth.models import AbstractUser
from .choices import GENDER_CHOICES

from django.db.models.signals import pre_save

# Create your models here.
class ExtendedUser(AbstractUser):
    gender = models.BooleanField(default=GENDER_CHOICES[0][0], choices=GENDER_CHOICES)
    image = models.ImageField(upload_to='avatars/', blank=True)
    url = models.URLField(blank=True)
    biography = models.CharField(max_length=1000, blank=True)

    def snippet(self):
        return self.biography[:130] + '...'


def set_avatar(instance):
    avatar = instance.image
    gender = instance.gender
    if gender == False:
        avatar = 'default_male.png'
    else:
        avatar = 'default_famale.png'
    return avatar

def post_save_avatar(sender, instance, *args, **kwargs):
    if not instance.image:
        instance.image = set_avatar(instance)
pre_save.connect(post_save_avatar, sender=ExtendedUser)
