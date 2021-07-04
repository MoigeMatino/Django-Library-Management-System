from django.urls import path

from .views import BookDetailView, BookListView, AddBookView, HomePageView, EditBookView, DeleteBookView

urlpatterns = [
    path('',HomePageView.as_view(), name='home'),
    path('book/<int:pk>/', BookDetailView.as_view(),name = 'book_detail'),
    path('/books',BookListView.as_view(), name='books'),    
    path('book/addbook', AddBookView.as_view(), name='add_book'),
    path('/book/<int:pk>/edit/', EditBookView.as_view(), name= 'edit_book'),
    path('/book/<int:pk>/deletebook', DeleteBookView.as_view(), name= 'delete_book')
    
    
]