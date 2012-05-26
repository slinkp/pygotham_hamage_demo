from django.db import models

# Create your models here.


class Entry(models.Model):

    author = models.CharField(max_length=256)

    title = models.CharField(max_length=256)

    body = models.TextField()


