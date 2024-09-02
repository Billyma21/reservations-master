from django import forms
from catalogue.models import Artist, Troupe

class ArtistTroupeForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = ['troupe']
        widgets = {
            'troupe': forms.Select()
        }