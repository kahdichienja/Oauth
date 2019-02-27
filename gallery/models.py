from django.db import models
from pyuploadcare.dj.models import ImageField
from pyuploadcare.dj.forms import FileWidget
from datetime import datetime
# Create your models here.


class Photo(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, max_length=255)
    created_at = models.DateTimeField(default = datetime.now, blank = True)
    photo = ImageField(blank=True, manual_crop="")

    def __str__(self):
        myTitle = self.title
        return myTitle