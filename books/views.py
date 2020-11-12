from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView
from django.db.models import Q

from .models import (
    Book, Author, Episode,
    PublishingHouse, Genre
)


class BookListView(LoginRequiredMixin, ListView):
    """Class with all books which used on index page"""
    
    template_name = 'books/index.html'
    paginate_by = 1
    context_object_name = 'books'
    queryset = Book.objects.prefetch_related(
        'authors', 'publishing_house', 'episode',
    )


class BookDetailView(LoginRequiredMixin, DetailView):
    """Class with book detail info"""

    model = Book
    template_name = 'books/book_detail.html'


class TemplateView(LoginRequiredMixin, ListView):
    """
    Template view for author, genre,
    publishing_house and episode view
    
    """

    paginate_by = 8
    context_object_name = 'books'        

    def get_prefetch_related_queryset(self):
        return Book.objects.prefetch_related(
            'authors', 'genres',
            'publishing_house', 'episode'
        )


class AuthorListView(TemplateView):
    """Author info view"""

    template_name = 'books/author_info.html'

    def get_queryset(self):
        return super().get_prefetch_related_queryset().filter(
            authors=self.kwargs['author_id']
        )

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['author'] = Author.objects.get(
            pk=self.kwargs['author_id']
        )

        return context


class PublishingHouseView(TemplateView):
    """Publishing house info view"""

    template_name = 'books/publishing_house_info.html'

    def get_queryset(self):
        return super().get_prefetch_related_queryset().filter(
            publishing_house=self.kwargs['publ_id']
        )

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['publ_house'] = PublishingHouse.objects.get(
            pk=self.kwargs['publ_id']
        )
        context['episodes'] = context['publ_house'].episodes.all()

        return context


class EpisodeView(TemplateView):
    """Episode's books view"""

    template_name = 'books/episode_books.html'

    def get_queryset(self):
        return super().get_prefetch_related_queryset().filter(
            episode=self.kwargs['episode_id']
        )

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['episode'] = Episode.objects.get(
            pk=self.kwargs['episode_id']
        )

        return context


class GenreView(TemplateView):
    """Genre's books view"""

    template_name = 'books/genre_books.html'

    def get_queryset(self):
        return super().get_prefetch_related_queryset().filter(
            genres=self.kwargs['genre_id']
        )

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['genre'] = Genre.objects.get(
            pk=self.kwargs['genre_id']
        )

        return context


class SearchBookAndAuthorView(ListView):
    model = Book
    template_name = 'books/search_book_and_author.html'
    context_object_name = 'books'

    def get_queryset(self):
        query = self.request.GET.get('q')

        return Book.objects.filter(
            Q(title__icontains=query) | Q(authors__name__icontains=query)
        )

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['query'] = self.request.GET.get('q')

        return context
