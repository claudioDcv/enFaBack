from django.contrib.auth.models import User
from rest_framework import serializers
from apps.musical_group.models import MusicalStyle, Song


# Serializers define the API representation.
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'is_staff')


class MusicalStyleSerializer(serializers.ModelSerializer):
    class Meta:
        model = MusicalStyle
        fields = ('id', 'name')


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'
