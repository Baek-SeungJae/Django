from django import forms
from .models import Musician, Album, Music

class MusicianForm(forms.ModelForm):
    class Meta:
        model = Musician
        fields = ['name','age']

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        exclude = ['musician']

class Music(forms.ModelForm):
    class Meta:
        model = Music
        exclude = ['album']