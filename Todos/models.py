from django.db import models
from datetime import datetime
# Create your models here.

class Todos(models.Model):
    # id          = models.AutoField(primary_key=True)
    name        = models.CharField(max_length=30)
    Task        = models.TextField(max_length=30)
    date        = models.DateTimeField(default = datetime.now, blank = True)
    is_complete = models.CharField(max_length = 5, default=True, blank = True)