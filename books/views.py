from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView

from .models import (
    Book, Author, Episode,
    PublishingHouse, Genre
)


class BookListView(LoginRequiredMixin, ListView):
    """Class with all books which used on index page"""
    
    template_name = 'books/index.html'
    paginate_by = 12
    context_object_name = 'books'
    queryset = Book.objects.prefetch_related(
        'authors', 'publishing_house', 'episode', 'genres'
    )


class BookDetailView(DetailView):
    """Class with book detail info"""

    model = Book
    template_name = 'books/book_detail.html'


class AuthorListView(ListView):
    """Author info view"""

    template_name = 'books/author_info.html'
    paginate_by = 8
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


class PublishingHouseView(ListView):
    """Publishing house info view"""

    template_name = 'books/publishing_house_info.html'
    paginate_by = 8
    context_object_name = 'books'

    def get_queryset(self):
        return Book.objects.filter(
            publishing_house=self.kwargs['publ_id']
        ).prefetch_related(
            'authors', 'genres',
            'publishing_house', 'episode'
        )

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['publ_house'] = PublishingHouse.objects.get(
            pk=self.kwargs['publ_id']
        )
        context['episodes'] = context['publ_house'].episodes.all()

        return context


class EpisodeView(ListView):
    """Episode's books view"""

    template_name = 'books/episode_books.html'
    paginate_by = 8
    context_object_name = 'books'

    def get_queryset(self):
        return Book.objects.filter(
            episode=self.kwargs['episode_id']
        ).prefetch_related(
            'authors', 'genres',
            'publishing_house', 'episode'
        )

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['episode'] = Episode.objects.get(
            pk=self.kwargs['episode_id']
        )

        return context
