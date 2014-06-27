import logging
import dateutil.parser as parser
from datetime import datetime

from django.core.exceptions import MultipleObjectsReturned
from django.views.generic.edit import UpdateView, CreateView
from django.views.generic.detail import DetailView
from django.shortcuts import render, get_object_or_404, redirect

from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from support.models import Profile, Battle
from support.serializers import ProfileSerializer, BattleSerializer

@api_view(['GET', 'POST'])
@authentication_classes((SessionAuthentication, BasicAuthentication))
@permission_classes((IsAuthenticated,))
def profile_list(request):
    if request.method == 'GET':
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles, many=True)
        return Response(serializer.data,
                        status=status.HTTP_200_OK)
        
    elif request.method == 'POST':
        serializer = ProfileSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return Response({'error': 'false',
                             'time': datetime.now(),
                             'userid': serializer.data['id'],
                             },
                            status=status.HTTP_201_CREATED)
    return Response({'error': 'true',
                     'time': datetime.now(),
                     'msg': serializer.errors,},
                    status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes((SessionAuthentication, BasicAuthentication))
@permission_classes((IsAuthenticated,))
def profile_detail(request, pk):
    try:
        profile = Profile.objects.get(pk=pk)
    except Profile.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
        
    if request.method == 'GET':
        serializer = ProfileSerializer(profile)
        return Response(serializer.data,
                        status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = ProfileSerializer(profile, data=request.DATA)
        serializer.save()
        return Response({'error': 'false',
                         'time': datetime.now()
                        },
                        status=status.HTTP_200_OK)
        
    elif request.method == 'DELETE':
        profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    return Response({'error': 'true',
                     'time': datetime.now(),
                     'msg': serializer.errors,},
                    status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@authentication_classes((SessionAuthentication, BasicAuthentication))
@permission_classes((IsAuthenticated,))
def profile_find(request):
    if request.method == 'GET':
        try:
            profiles = Profile.objects.filter(nickname=request.GET['nickname'])
            if len(profiles) == 1:
                return redirect('profile-detail', pk=profiles[0].id)
            else:
                serializer = ProfileSerializer(profiles, many=True)
                return Response(serializer.data,
                                status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

    return Response({'error': 'true',
                     'time': datetime.now(),},
                    status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST', 'GET'])
@authentication_classes((SessionAuthentication, BasicAuthentication))
@permission_classes((IsAuthenticated,))
def battle_detail(request):
    if request.method == 'POST':
        INFO = request.DATA.copy()
        INFO['start'] = str(parser.parse(request.DATA['start']))
        INFO['end'] = str(parser.parse(request.DATA['end']))
        serializer = BattleSerializer(data=INFO)
        if serializer.is_valid():
            serializer.save()
            return Response({'error': 'false',
                             'time': datetime.now(),
                             },
                            status=status.HTTP_201_CREATED)
    if request.method == 'GET':
        try:
            if request.GET:
                start = parser.parse(request.GET['start'])
                end = parser.parse(request.GET['end'])
                battles = Battle.objects.filter(start__gt=start,
                                                end__lt=end)
            else:
                battles = Battle.objects.all()
        except:
            pass

        serializer = BattleSerializer(battles, many=True)
        return Response(serializer.data,
                        status=status.HTTP_200_OK)

    return Response({'error': 'true',
                     'time': datetime.now(),},
                    status=status.HTTP_400_BAD_REQUEST)
