from django.shortcuts import render
from django.views.generic import TemplateView
from apps.musical_group.models import MusicalGroup, Song
from django.db.models import Q
from django.shortcuts import redirect


class HomeView(TemplateView):
    template_name = 'musical_group/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['user'] = self.request.user
        context['musical_groups'] = MusicalGroup.objects.filter(
            directors__user_id=self.request.user.pk
        )
        context['musical_groups_permanent'] = MusicalGroup.objects.filter(
            permanent_musician__user_id=self.request.user.pk
        )
        context['musical_groups_guest'] = MusicalGroup.objects.filter(
            guest_musician__user_id=self.request.user.pk
        )
        return context


class MusicalGroupView(TemplateView):
    template_name = 'musical_group/group.html'

    def get_context_data(self, **kwargs):
        context = super(MusicalGroupView, self).get_context_data(**kwargs)
        context['user'] = self.request.user
        context['musical_group'] = MusicalGroup.objects.get(
            pk=kwargs['group_id'],
            directors__user_id=self.request.user.pk
        )
        context['songs'] = context['musical_group'].songs.all()
        return context


class MusicalGroupPermanentView(TemplateView):
    template_name = 'musical_group/group.html'

    def get_context_data(self, **kwargs):
        context = super(MusicalGroupPermanentView, self).get_context_data(**kwargs)
        context['user'] = self.request.user
        context['musical_group'] = MusicalGroup.objects.get(
            pk=kwargs['group_id'],
            permanent_musician__user_id=self.request.user.pk
        )
        context['songs'] = context['musical_group'].songs.all()
        return context


class MusicalGroupGuestView(TemplateView):
    template_name = 'musical_group/group.html'

    def get_context_data(self, **kwargs):
        context = super(MusicalGroupGuestView, self).get_context_data(**kwargs)
        context['user'] = self.request.user
        # import ipdb; ipdb.set_trace()
        context['musical_group'] = MusicalGroup.objects.get(
            pk=kwargs['group_id'],
            guest_musician__user_id=self.request.user.pk
        )
        # import ipdb; ipdb.set_trace()
        context['songs'] = context['musical_group'].songs.all()
        return context


class SongView(TemplateView):
    template_name = 'musical_group/song.html'

    def get_context_data(self, **kwargs):
        context = super(SongView, self).get_context_data(**kwargs)
        context['user'] = self.request.user
        context['song'] = Song.objects.filter(
            Q(musical_group__directors__user_id=self.request.user.pk) |
            Q(guest_musician__user_id=self.request.user.pk) |
            Q(permanent_musician__user_id=self.request.user.pk)
        ).filter(pk=kwargs['song_id']).first()
        return context


    def get(self, request, **kwargs):
        context = self.get_context_data(**kwargs)
        if context['song']:
            return self.render_to_response(context)
        return redirect('home')
