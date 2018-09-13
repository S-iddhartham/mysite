# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
# from django.views.generic import ListView
from books.models import Publisher

from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from books.models import Book, Publisher

# Create your views here.
class PublisherList(ListView):
    model = Publisher 
    context_object_name = 'my_favorite_publishers'

class PublisherBookList(ListView):

    template_name = 'books/books_by_publisher.html'

    def get_queryset(self):
        self.publisher = get_object_or_404(Publisher,  name=self.args[0])
        return Book.objects.filter(publisher=self.publisher)
