from django.conf.urls import url, include
from rest_framework import routers
from apps.api.views import UserViewSet, MusicalStyleViewSet, SongViewSet, \
    MusicalInstrumentViewSet, UserMusicalInstrumentStyleViewSet


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'musical-styles', MusicalStyleViewSet)
router.register(r'songs', SongViewSet)
router.register(r'users-musical-instrument-style', UserMusicalInstrumentStyleViewSet)
router.register(r'musical-instrument', MusicalInstrumentViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
