from django.contrib import admin

from . models import *


class format1(admin.ModelAdmin):
    list_display = ('url', 'author', 'tags_author', 'tags_playlist', 'text', 'link', 'image')

admin.site.register(Playlist,format1)
# Register your models here.
