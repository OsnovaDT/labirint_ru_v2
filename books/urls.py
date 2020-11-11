from django.urls import path

from .views import BookListView


app_name = 'books'

urlpatterns = [
    # Index page with all books
    path('', BookListView.as_view(), name='index'),
]
