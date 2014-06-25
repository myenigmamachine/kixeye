from django.db import models
from django.contrib.auth.models import User


class ProfileManager(models.Manager):
    def create_profile(self, nick_name,
                       first_name,
                       last_name,
                       wins,
                       losses,
                       win_streak,
                       created,
                       last_seen):
        profile = self.create(username=nick_name,
                              first_name = first_name,
                              last_name = last_name,
                              wins = wins,
                              losses = losses,
                              win_streak = win_streak,
                              created = created,
                              last_seen = last_seen,)

class Profile(User):
    objects = ProfileManager()
    nick_name = models.CharField(max_length=255)
    wins = models.IntegerField()
    losses = models.IntegerField()
    win_streak = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    last_seen = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "support_profile"