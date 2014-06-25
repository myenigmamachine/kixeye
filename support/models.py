from django.db import models
from django.contrib.auth.models import User

class Profile(User):
    nick_name = models.CharField(max_length=255)
    wins = models.IntegerField()
    losses = models.IntegerField()
    win_streak = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    last_seen = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "support_profile"