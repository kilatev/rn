from django.db import models


class Channel(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    link = models.CharField(max_length=2083, unique=True)
    lastBuildDate = models.DateTimeField()
    generator = models.CharField(max_length=255)
    language = models.CharField(max_length=6)


class Item(models.Model):
    title = models.CharField(max_length=255)
    link = models.CharField(max_length=2083)
    guid = models.CharField(max_length=36, unique=True)
    description = models.TextField()
    author = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    pubDate = models.DateTimeField()
    channel = models.ForeignKey(Channel)