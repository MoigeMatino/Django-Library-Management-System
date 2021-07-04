from django.shortcuts import render
from django.views.generic import ListView, TemplateView, DetailView
from django.views.generic.edit import  CreateView, UpdateView, DeleteView
from .models import *
from django.urls import reverse_lazy

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'

class BookListView(ListView):
    model = Book
    template_name = 'books.html'
    context_object_name = 'books_list'

class BookDetailView(DetailView):
    model = Book
    template_name = 'book_detail.html'

class AddBookView(CreateView):
    model = Book
    template_name = 'add_book.html'
    fields = ['title','author','genre','isbn']

class EditBookView(UpdateView):
    model = Book
    template_name = 'edit_book.html'
    fields = ['title','author','genre','isbn']

class DeleteBookView(DeleteView):
    model = Book
    template_name = 'delete_book.html'
    success_url = reverse_lazy('books')