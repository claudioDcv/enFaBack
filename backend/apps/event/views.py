from django.contrib.auth.models import User
from rest_framework import viewsets
from apps.event.serializers import EventSerializer
from apps.event.models import Event
from django.db.models import Q
import datetime


class EventViewSet(viewsets.ModelViewSet):
    '''
    ?start_dt=1510284123937&end_dt=1541820123937
    '''
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def get_queryset(self):

        queryset = self.queryset
        start_dt = self.request.query_params.get('start_dt', 0)
        end_dt = self.request.query_params.get('end_dt', 0)
        if start_dt is not 0 and end_dt is not 0:

            start_dt = datetime.datetime.fromtimestamp(int(start_dt)/1000)
            end_dt = datetime.datetime.fromtimestamp(int(end_dt)/1000)

            queryset = queryset.filter(
                Q(start_dt__range=[start_dt, end_dt]) |
                Q(end_dt__range=[start_dt, end_dt])
            )
        else:
            queryset = queryset[:100]
        return queryset
