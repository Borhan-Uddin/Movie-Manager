from ast import mod
from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name


class Movie(models.Model):
    name = models.CharField(max_length=100)
    published_year = models.PositiveIntegerField()
    genre = models.ManyToManyField(Genre, related_name='genre')
    watched = models.BooleanField(default= False)

    def __str__(self) -> str:
        return self.name