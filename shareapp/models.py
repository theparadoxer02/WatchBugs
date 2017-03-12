from __future__ import unicode_literals

from django.db import models

# Create your models here.
class bugshare(models.Model):
    name = models.CharField(max_length=40,null=True,blank=True,unique=True)
    url = models.URLField(max_length=50,null=True)
    code = models.CharField(max_length=1000,null=True)
    bug = models.CharField(max_length=100,null=True,blank=True)
    comment = models.CharField(max_length=100,null=True,blank=True)
    hash_value = models.SlugField(max_length=100,null=True,blank=True,unique=True)

    def __unicode__(self):
        return str(self.name)
