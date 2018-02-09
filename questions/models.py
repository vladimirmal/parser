from __future__ import unicode_literals

from django.db import models
from django.contrib.postgres.fields import ArrayField


# Create your models here.
class SaveUrl(models.Model):
    url = models.CharField(max_length=1000)

class Questions(models.Model):

    title = models.CharField(max_length=512)
    identifier =models.CharField(max_length=256)
    url = models.CharField(max_length=1024)

    def __unicode__(self):
        return "{} - {}".format(self.identifier,self.title)

class Tasks(models.Model):
    url = models.CharField(max_length=100)
    ip = models.GenericIPAddressField()
    date = models.DateTimeField(auto_now=True)