from django.contrib import admin
from .models import Genre, Movies


class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
# Register your models here.
admin.site.register(Genre, GenreAdmin)
admin.site.register(Movies)