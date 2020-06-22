from django.db import models

# Create your models here.


class Musician(models.Model):
    name = models.CharField(max_length=150)
    age = models.IntegerField()


class Album(models.Model):
    name = models.CharField(max_length=150)
    musician = models.ForeignKey(Musician, on_delete=models.CASCADE)
    created_at = models.DateField()
    musicVideo = models.CharField(max_length=150)
    cover = models.CharField(max_length=150)


class Music(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    like = models.IntegerField(default=0)
