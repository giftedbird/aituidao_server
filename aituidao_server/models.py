# -*- coding: utf-8 -*-

from django.db import models

class Book(models.Model):
    title = models.CharField(max_length = 100)
    author = models.CharField(max_length = 100)
    intro = models.CharField(max_length = 1000, blank=True, null=True)
    cover = models.CharField(max_length = 100, blank=True, null=True)
    coverUrl = models.CharField(max_length = 1000, blank=True, null=True)
    filename = models.CharField(max_length = 100)
    pushCount = models.IntegerField()
    doubanRate = models.IntegerField()
    uploadUserId = models.IntegerField();
