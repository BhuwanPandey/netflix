from django.contrib import admin
from .models import MovieList,Movies
from imagekit.admin import AdminThumbnail

class MovieAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'admin_thumbnail')
    admin_thumbnail = AdminThumbnail(image_field='image_thumbnail')

admin.site.register(Movies,MovieAdmin)
admin.site.register(MovieList)

