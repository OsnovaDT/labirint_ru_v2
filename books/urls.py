from django.urls import path

from .views import (
    BookListView, BookDetailView, AuthorListView
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
]
