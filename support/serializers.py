from support.models import Profile, Battle
from rest_framework import serializers


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ('id',
                  'url',
                  'first',
                  'last',
                  'nickname',
                  'wins',
                  'losses',
                  'win_streak',
                  'created',
                  'last_seen',)

class BattleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Battle
        fields = ('attacker',
                  'defender',
                  'winner',
                  'start',
                  'end',)