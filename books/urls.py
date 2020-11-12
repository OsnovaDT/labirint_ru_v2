from django.urls import path

from .views import (
    BookListView, BookDetailView, AuthorListView,
    PublishingHouseView, EpisodeView
)


app_name = 'books'

urlpatterns = [
    # Index page with all books
    path('', BookListView.as_view(), name='index'),

    # Book detail info
    path(
        'book/<int:pk>/',
        BookDetailView.as_view(),
        name='book_detail_info'
    ),

    # Author info
    path(
        'author/<int:author_id>/',
        AuthorListView.as_view(),
        name='author_info'
    ),

    # Publishing house info
    path(
        'publishing_house/<int:publ_id>/',
        PublishingHouseView.as_view(),
        name='publishing_house_info'
    ),
    
    # Episode's books
    path(
        'episode/<int:episode_id>/',
        EpisodeView.as_view(),
        name='episode_books'
    ),
]
