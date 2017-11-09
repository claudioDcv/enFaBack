from django.contrib.auth.models import User
from rest_framework import serializers
from apps.musical_group.models import MusicalStyle, Song, MusicalInstrument, \
    UserMusicalInstrumentStyle


# Serializers define the API representation.
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'is_staff')


class MusicalInstrumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = MusicalInstrument
        fields = '__all__'


class MusicalStyleSerializer(serializers.ModelSerializer):
    class Meta:
        model = MusicalStyle
        fields = ('id', 'name')


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'


class UserMusicalInstrumentStyleSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    user_id = UserSerializer(write_only=True)
    musical_instruments = MusicalInstrumentSerializer(read_only=True)
    musical_instruments_id = MusicalInstrumentSerializer(write_only=True)

    class Meta:
        model = UserMusicalInstrumentStyle
        fields = '__all__'
