from rest_framework import serializers

from django.contrib.auth.models import Group

from core.models.user import User
from core.models.church import Church
from core.models.wing import Wing
from core.models.due import Due


class ChurchSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:

        model = Church

        fields = ('url', 'denomination')


class GroupSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:

        model = Group

        fields = ('url', 'name')


class UserSerializer(serializers.HyperlinkedModelSerializer):

    password = serializers.CharField(write_only = True, style = { 'input_type': 'password' })

    class Meta:

        model = User

        fields = ('url', 'username', 'password', 'email', 'is_staff', 'is_superuser', 'date_joined', 'wings')


class DueSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:

        model = Due

        fields = ('url', 'user', 'wing', 'offer')


class WingSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:

        model = Wing

        fields = ('url', 'wing', 'church')
