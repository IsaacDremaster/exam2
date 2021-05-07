from django.db import models


class Universe(models.Model):
    name = models.CharField(max_length=200)


class Team(models.Model):
    character_universe = models.ForeignKey(Universe, models.SET_NULL, 'character', null=True)
    name = models.CharField('Имя персонажа', max_length=100)
    gender = models.CharField('Пол', max_length=6)
    ability = models.CharField('Способности', max_length=100)