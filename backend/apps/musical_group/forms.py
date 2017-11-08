from django import forms
from apps.musical_group.models import Song


class SongForm(forms.ModelForm):
    name = forms.CharField(
        label='Nombre',
        max_length=100,
        widget=forms.TextInput(attrs={
            'autocomplete': 'off',
            'class': 'form-control',
        }),
    )
    color = forms.CharField(
        label='Color',
        max_length=10,
        widget=forms.TextInput(attrs={
            'autocomplete': 'off',
            'class': 'form-control jscolor',
        }),
    )

    # musical_styles = forms.MultipleChoiceField(
    #     widget=forms.SelectMultiple(attrs={
    #         'class': 'form-control js-data-example-ajax',
    #     }),
    # )

    class Meta:
        model = Song  # with attr somedata
        fields = '__all__'
        exclude = ('musical_styles',)

    def valid_color(self):
        # send email using the self.cleaned_data dictionary
        pass
