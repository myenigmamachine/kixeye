import logging

from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class Profile(AbstractBaseUser):
    nickname = models.CharField(max_length=255, default='')
    first = models.CharField(max_length=255, default='')
    last = models.CharField(max_length=255, default='')
    wins = models.IntegerField(default=0)
    losses = models.IntegerField(default=0)
    win_streak = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    last_seen = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'nickname'

    class Meta:
        db_table = "support_profile"


class Battle(models.Model):
    attacker = models.IntegerField(default=0)
    defender = models.IntegerField(default=0)
    winner = models.IntegerField(default=0)
    start = models.DateTimeField()
    end = models.DateTimeField()
    class Meta:
        db_table = "support_battle"