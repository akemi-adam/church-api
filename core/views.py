from django.contrib.auth.models import Group

from rest_framework import permissions
from rest_framework import viewsets

from core.serializers import ChurchSerializer, GroupSerializer, UserSerializer, WingSerializer, DueSerializer

from core.models.church import Church
from core.models.user import User
from core.models.wing import Wing
from core.models.due import Due


class ChurchViewSet(viewsets.ModelViewSet):
    
    queryset = Church.objects.all().order_by('denomination')

    serializer_class = ChurchSerializer

    permission_classes = [ permissions.IsAuthenticated, permissions.IsAdminUser ]


class GroupViewSet(viewsets.ModelViewSet):
    
    queryset = Group.objects.all()

    serializer_class = GroupSerializer

    permission_classes = [ permissions.IsAuthenticated, permissions.IsAdminUser ]


class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()

    serializer_class = UserSerializer

    permission_classes = [ permissions.IsAuthenticated, permissions.IsAdminUser ]


class WingViewSet(viewsets.ModelViewSet):

    queryset = Wing.objects.all()

    serializer_class = WingSerializer

    permission_classes = [ permissions.IsAuthenticated, permissions.IsAdminUser ]

    def get_permissions(self):

        if self.request.method == 'GET':
            return [ permissions.IsAuthenticated() ]
        else:
            return super().get_permissions()


class DueViewSet(viewsets.ModelViewSet):

    queryset = Due.objects.all()

    serializer_class = DueSerializer

    permission_classes = [ permissions.IsAuthenticated ]