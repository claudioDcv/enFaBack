from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.decorators import login_required, permission_required
from apps.musical_group.views import HomeView, MusicalGroupView, MusicalGroupPermanentView, MusicalGroupGuestView, SongView, SongEditView
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^home/$', login_required(HomeView.as_view()), name='home'),
    url(
        r'^home/group/(?P<group_id>\w{0,50})/$',
        login_required(MusicalGroupView.as_view()),
        name='group',
    ),
    url(
        r'^home/group-permanent-musician/(?P<group_id>\w{0,50})/$',
        login_required(MusicalGroupPermanentView.as_view()),
        name='group-permanent-musician',
    ),
    url(
        r'^home/group-guest-musician/(?P<group_id>\w{0,50})/$',
        login_required(MusicalGroupGuestView.as_view()),
        name='group-guest-musician',
    ),
    url(
        r'^home/song/(?P<song_id>\w{0,50})/$',
        login_required(SongView.as_view()),
        name='song',
    ),
    url(
        r'^home/song/(?P<pk>\w{0,50})/edit/$',
        login_required(SongEditView.as_view()),
        name='song-edit',
    ),
    url(r'^api/', include('apps.api.urls', namespace='api'))
]
