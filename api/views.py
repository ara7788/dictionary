
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import ApiSerializer, UserSerializer, GroupSerializer
from .models import Api
from django.contrib.auth.decorators import login_required


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class ApiViewSet(viewsets.ModelViewSet):
    queryset = Api.objects.all().order_by('name')
    serializer_class = ApiSerializer
    permission_classes = [permissions.IsAuthenticated]
