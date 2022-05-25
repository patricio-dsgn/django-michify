from django.contrib import admin

from . models import *


class format1(admin.ModelAdmin):
    list_display = ('url', 'author', 'tags_author', 'tags_playlist', 'text', 'link', 'image')

admin.site.register(Playlist,format1)
# Register your models here.



class table_format1(admin.ModelAdmin):
    list_display = ('title', 'text', 'photo')
class table_format2(admin.ModelAdmin):
    list_display = ('title', 'icon', 'text',)
class table_format3(admin.ModelAdmin):
    list_display = ('full_name', 'email')

class table_format4(admin.ModelAdmin):
    list_display = ('typesb', 'text', 'cause', 'photo')

# admin.site.register(Tip, table_format2)
admin.site.register(Post, table_format1)
admin.site.register(Suscriptor, table_format3)

admin.site.register(Contact)