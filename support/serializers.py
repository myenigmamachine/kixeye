from support.models import Profile
from rest_framework import serializers


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ('url',
                  'first_name',
                  'last_name',
                  'username',
                  'wins',
                  'losses',
                  'win_streak',
                  'created',
                  'last_seen',)
