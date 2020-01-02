from django.db import models

# Create your models here.
from django.utils import timezone


class ToDo(models.Model):
    text = models.CharField(max_length=60, null=True)

    def __str__(self):
        return self.text
