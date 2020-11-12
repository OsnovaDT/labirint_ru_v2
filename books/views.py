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
    paginate_by = 1
    context_object_name = 'books'
    queryset = Book.objects.prefetch_related(
        'authors', 'publishing_house', 'episode', 'genres'
    )


class BookDetailView(DetailView):
    """Class with book detail info"""

    model = Book
    template_name = 'books/book_detail.html'


class AuthorListView(ListView):
    """Class with all author's books"""

    template_name = 'books/author_books.html'
    paginate_by = 2
    context_object_name = 'books'
    
    def get_queryset(self):
        return Book.objects.filter(
            authors=self.kwargs['author_id']
        ).prefetch_related(
            'authors', 'genres',
            'publishing_house', 'episode'
        )

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['author'] = Author.objects.get(
            pk=self.kwargs['author_id']
        )

        return context
