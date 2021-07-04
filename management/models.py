from django.db import models
from django.urls import reverse


#model defining student information
class Student(models.Model):
    name = models.CharField(max_length=40)
    id_no = models.CharField(max_length=10)
    email = models.EmailField(unique = True)

    def __str__(self):
        return self.name
    
    # def get_absolute_url(self):
    #     return reverse()
    
#model defining book information
class Book(models.Model):
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=50)
    genre = models.CharField(max_length=20)
    isbn = models.CharField('ISBN',max_length=13, help_text='Enter a 13 character book identifier <a href = "https://www.isbn.ac.ke/">ISBN number</a>')
    

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('book_detail', args=[str(self.pk)])


