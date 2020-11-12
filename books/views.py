from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView

from .models import (
    Book, Author, Episode,
    PublishingHouse, Genre
)


# For index page
class BookListView(LoginRequiredMixin, ListView):
    """Class with all books which used on index page"""
    
    template_name = 'books/index.html'
    paginate_by = 2
    context_object_name = 'books'
    queryset = Book.objects.prefetch_related(
        'authors', 'publishing_house', 'episode', 'genres'
    )


class BookDetailView(DetailView):
    model = Book
    template_name = 'books/book_detail.html'
