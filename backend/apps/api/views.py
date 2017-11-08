from django.contrib.auth.models import User
from rest_framework import viewsets
from apps.api.serializers import UserSerializer, MusicalStyleSerializer
from apps.musical_group.models import MusicalStyle


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class MusicalStyleViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = MusicalStyle.objects.all()
    serializer_class = MusicalStyleSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = self.queryset
        q = self.request.query_params.get('q', None)
        if q is not None:
            queryset = queryset.filter(name__icontains=q)
        else:
            queryset = queryset[:10]
        return queryset
