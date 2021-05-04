from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView

from django_books.models import Author


class AuthorListView(ListView):
    model = Author
    template_name = 'author/author_list.html'

    def get_queryset(self):
        return Author.objects.all()


class AuthorDetailView(DetailView):
    model = Author
    template_name = 'author/author_detail_list.html'
