from django.db import models

# Create your models here.
class Author(models.Model):
    AuthorID = models.CharField(max_length=50, primary_key=True)
    Name = models.CharField(max_length=50)
    Age = models.CharField(max_length=50)
    Country = models.CharField(max_length=50)
    
class Book(models.Model):
    ISBN = models.CharField(max_length=50, primary_key=True)
    Title = models.CharField(max_length=50)
    AuthorID = models.ForeignKey(Author, db_column = 'AuthorID')
    Publisher = models.CharField(max_length=50)
    PublishDate = models.CharField(max_length=50)
    Price = models.CharField(max_length=50)
    

