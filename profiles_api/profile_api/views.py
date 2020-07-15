from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated

from profile_api import serializers
from profile_api import models
from profile_api import permissions
    
class UserProfileViewSet(viewsets.ModelViewSet):
    """Model view set"""
    serializer_class = serializers.UserProfileSerializers
    queryset = models.UserProfile.object.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ("name", "email")
    
class UserApiLoginView(ObtainAuthToken):
    """Handle user authentication toke"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
    
    
