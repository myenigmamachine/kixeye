from support.models import Profile
from rest_framework import viewsets
from support.serializers import ProfileSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer