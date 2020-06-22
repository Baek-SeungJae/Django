from django.contrib import admin
from .models import Musician, Album, Music
# Register your models here.


class MusicianAdmin(admin.ModelAdmin):
    list_display = ('name', 'age')


admin.site.register(Musician, MusicianAdmin)


class AlbumAdmin(admin.ModelAdmin):
    list_display = ('name', 'musician', 'created_at', 'musicVideo', 'cover')


admin.site.register(Album, AlbumAdmin)


class MusicAdmin(admin.ModelAdmin):
    list_display = ('album', 'name', 'like')


admin.site.register(Music, MusicAdmin)
