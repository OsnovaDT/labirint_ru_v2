from django.contrib import admin

from books.models import (
    Book, Genre, Author,
    PublishingHouse, Episode
)


class BookAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'get_authors', 'publishing_house',
        'episode', 'price', 'get_genres'
    )
    list_display_links = (
        'title', 'get_authors', 'publishing_house',
        'episode', 'get_genres'
    )
    search_fields = (
        'title', 'get_authors', 'publishing_house',
        'episode', 'get_genres'
    )


class EpisodeAdmin(admin.ModelAdmin):
    list_display = ('name', 'publishing_house')
    list_display_links = ('name', 'publishing_house')
    search_fields = ('name', 'publishing_house')


class PublishingHouseAdmin(admin.ModelAdmin):
    list_display = ('name', 'info',)
    list_display_links = ('name',)
    search_fields = ('name',)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'info',)
    list_display_links = ('name',)
    search_fields = ('name',)


admin.site.register(Book, BookAdmin)
admin.site.register(Episode, EpisodeAdmin)
admin.site.register(
    PublishingHouse, PublishingHouseAdmin
)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Genre)
