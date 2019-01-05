import uuid
from colorful.fields import RGBColorField
from ckeditor.fields import RichTextField

from .choices import STATE_CHOICES
from .utils import get_unique_slug

from django.db import models
from django.conf import settings
from django.urls import reverse
from django.db.models.signals import pre_save

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
    slug = models.SlugField(max_length=140, unique=True, blank=True)
    state = models.IntegerField(default=STATE_CHOICES[0][0], choices=STATE_CHOICES)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    cat = models.ForeignKey(Category, to_field='identy', on_delete=models.CASCADE, default=1)
    thumb = models.ImageField(default="default.png")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:view', kwargs={'pk': self.id, 'slug': self.slug})

    def snippet(self):
        return self.body[:250] + '...'

def post_save_slug(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = get_unique_slug(instance, 'title', 'slug')

pre_save.connect(post_save_slug, sender=Post)