

from django.utils import timezone
from django.db import models

# Create your models here.

class taskD(models.Model):
    task = models.CharField(max_length=30)
    desription = models.CharField(max_length=50)
    completed = models.BooleanField(default=False)
    created_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "%s %s"%(self.task,self.desription)