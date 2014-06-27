import logging
from datetime import datetime

from django.test import TestCase
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from rest_framework.test import APIClient
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from support.models import Profile

class ProfileTests(APITestCase):
    user1 = {
        'nickname': 'user1',
        'last': 'lastname',
        'first': 'firstname',
    }
    user2 = {
        'nickname': 'user2',
        'last': 'lastname',
        'first': 'firstname',
    }
    battle1 = {
        'attacker': '1',
        'defender': '2',
        'winner': '1',
        'start': '2014-06-27T10:47:12.502',
        'end': '2014-06-27T10:48:33.106',
    }
    battle2 = {
        'attacker': '2',
        'defender': '1',
        'winner': '1',
        'start': '2014-06-27T10:45:47.311',
        'end': '2014-06-27T10:47:55.768',
    }

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user('testuser',
                                             email='testuser@test.com',
                                             password='testing')
        self.user.save()
        self.client.force_authenticate(user=User.objects.get(username='testuser'))
        
    def test_create_profile(self):
        self.client.login(username='testuser', password='testing')
        url = reverse('profile-list')
        response1 = self.client.post(url, self.user1)
        self.assertEqual(response1.status_code, status.HTTP_201_CREATED)
        self.assertEqual((response1.data['error'] is 'false'), True)

        response2 = self.client.post(url, self.user2)
        self.assertEqual(response2.status_code, status.HTTP_201_CREATED)
        self.assertEqual((response2.data['error'] is 'false'), True)

    def test_update_profile(self):
        self.client.login(username='testuser', password='testing')
        Profile.objects.create(nickname=self.user1['nickname'], 
                               last=self.user1['last'],
                               first=self.user1['first'])
        Profile.objects.create(nickname=self.user2['nickname'], 
                               last=self.user2['last'],
                               first=self.user2['first'])
        profile1 = Profile.objects.get(nickname=self.user1['nickname'])
        profile1.save()
        profile2 = Profile.objects.get(nickname=self.user2['nickname'])
        profile2.save()
        url1 = reverse('profile-detail', kwargs={'pk': profile1.id})
        url2 = reverse('profile-detail', kwargs={'pk': profile2.id})

        self.user1_orig = self.user1.copy()
        self.user2_orig = self.user2.copy()        

        response1 = self.client.put(url1,
                                    {'nickname': self.user2['nickname']})
        self.assertEqual(response1.status_code, status.HTTP_200_OK)
        self.assertEqual((response1.data['error'] is 'false'), True)

        response2 = self.client.put(url2,
                                    {'nickname':self.user1['nickname']})
        self.assertEqual(response2.status_code, status.HTTP_200_OK)
        self.assertEqual((response2.data['error'] is 'false'), True)

    def test_create_battle(self):
        self.client.login(username='testuser', password='testing')
        url = reverse('battle-detail')

        response1 = self.client.post(url, self.battle1)
        self.assertEqual(response1.status_code, status.HTTP_201_CREATED)
        self.assertEqual((response1.data['error'] is 'false'), True)
        response2 = self.client.post(url, self.battle2)
        self.assertEqual(response2.status_code, status.HTTP_201_CREATED)
        self.assertEqual((response2.data['error'] is 'false'), True)


class BattleTests(APITestCase):
    pass
