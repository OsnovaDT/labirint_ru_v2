from django.urls import path

from .views import BookListView, BookDetailView


app_name = 'books'

urlpatterns = [
    # Index page with all books
    path('', BookListView.as_view(), name='index'),

    # Book detail
    path(
        'book/<int:pk>/',
        BookDetailView.as_view(),
        name='book_detail_info'
    )
]
