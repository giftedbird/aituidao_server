# -*- coding: utf-8 -*-

from django.db import models

class Book(models.Model):
    title = models.CharField(max_length = 100)
    author = models.CharField(max_length = 100)
    intro = models.CharField(max_length = 1000, blank=True, null=True)
    coverUrl = models.URLField(blank=True, null=True);
    pushCount = models.IntegerField();
    doubanRate = models.FloatField();
    deleted = models.BooleanField();
