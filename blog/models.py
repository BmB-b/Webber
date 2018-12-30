import uuid
from colorful.fields import RGBColorField
from ckeditor.fields import RichTextField

from .choices import STATE_CHOICES

from django.db import models
from django.conf import settings

# Create your models here.
class Category(models.Model):

    identy = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    color = RGBColorField(default="#000000")

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Post(models.Model):

    title = models.CharField(max_length=60)
    body = RichTextField(max_length=10000)
    pub_date = models.DateField()
    state = models.IntegerField(default=STATE_CHOICES[0][0], choices=STATE_CHOICES)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    cat = models.ForeignKey(Category, to_field='identy', on_delete=models.CASCADE, default=1)
    thumb = models.ImageField(default="default.png")

    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:250] + '...'