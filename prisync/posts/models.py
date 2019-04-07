# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class posts(models.Model):
    title = models.TextField()
    link = models.TextField()
    category = models.TextField()
    creator = models.TextField()
    pubdate = models.TextField()
    description = models.TextField()
