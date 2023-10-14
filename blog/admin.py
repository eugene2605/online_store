from django.contrib import admin
from blog.models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'date_of_creation', 'is_published')
    list_filter = ('date_of_creation',)
    search_fields = ('date_of_creation', 'is_published')
