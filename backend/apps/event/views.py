from rest_framework import viewsets
from apps.event.serializers import EventSerializer
from apps.event.models import Event
from django.db.models import Q


class EventViewSet(viewsets.ModelViewSet):
    '''
    ?start_dt=1510284123937&end_dt=1541820123937
    '''
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def get_queryset(self):
        queryset = self.queryset
        start = self.request.query_params.get('start', 0)
        end = self.request.query_params.get('end', 0)
        user = self.request.user
        if start is not 0 and end is not 0 and user:

            queryset = queryset.filter(
                Q(start__range=[start, end]) |
                Q(end__range=[start, end])
            ).filter(users__user__pk=user.id)
        else:
            queryset = queryset[:100]
        return queryset
