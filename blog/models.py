import uuid
from colorful.fields import RGBColorField

from django.db import models

# Create your models here.
class Category(models.Model):

    identy = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    color = RGBColorField(default="#000000")

    def __str__(self):
        return self.name