from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import *

class BookTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
                    username='testuser',
                    email='test@email.com',
                    password='secret'
        )

        self.book = Book.objects.create(
            title='A good title',
            author=self.user,
            genre='best genre',
            isbn = 1111111111111
                    
        )
    def test_string_representation(self):
        book = Book(title='A sample title') 
        self.assertEqual(str(book), book.title)

    def test_get_absolute_url(self): 
        self.assertEqual(self.book.get_absolute_url(), '/book/1/')

    def test_book_content(self): 
        self.assertEqual(f'{self.book.title}', 'A good title') 
        self.assertEqual(f'{self.book.author}', 'testuser') 
        self.assertEqual(f'{self.book.genre}', 'best genre')

    def test_book_list_view(self):
        response = self.client.get(reverse('books')) 
        self.assertEqual(response.status_code, 200) 
        self.assertTemplateUsed(response, 'books.html')

    def test_book_detail_view(self):
        response = self.client.get('/book/1/')
        no_response = self.client.get('/book/100000/') 
        self.assertEqual(response.status_code, 200) 
        self.assertEqual(no_response.status_code, 404) 
        self.assertContains(response, 'A good title') 
        self.assertTemplateUsed(response, 'book_detail.html')

    def test_add_book_view(self):
        response = self.client.get(reverse('add_book'), {
                    'title': 'New title',
                    'author': self.user,
                    'genre': 'Best genre',
                    'isbn': 1111111111111,
                })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'New title')
        self.assertContains(response, 'Best genre')
        self.assertContains(response, 1111111111111)

    def test_update_book_view(self): 
        response = self.client.book(reverse('edit_book', args='1'), {
                    'title': 'Updated title',
                    'author': 'Updated author',
                    'genre': 'Updated genre',
                    'isbn': 1111111111111,
                })
        self.assertEqual(response.status_code, 302)

    def test_delete_book_view(self): # new 
        response = self.client.get(
        reverse('delete_book', args='1'))
        self.assertEqual(response.status_code, 200)