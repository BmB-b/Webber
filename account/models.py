from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class ExtendedUser(AbstractUser):
    image = models.ImageField(upload_to='avatars/')
    url = models.URLField()
    biography = models.CharField(max_length=1000)

    def snippet(self):
        return self.biography[:130] + '...'