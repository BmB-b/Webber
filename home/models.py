from django.db import models
from blog.models import Category

# Create your models here.
class Widget(models.Model):

    state = models.BooleanField(default=False)
    name = models.CharField(max_length=20)
    desc = models.TextField(max_length=250)
    content = models.ForeignKey(Category, to_field='identy', on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name