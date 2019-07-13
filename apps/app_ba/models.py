from django.db import models

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    notes = models.TextField(max_length = 255)

    def __repr__(self):
        return f"<Author: {self.first_name} {self.last_name}>"


class Book(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField(max_length = 500)
    authors = models.ManyToManyField(Author, related_name="books")

    def __repr__(self):
        return f"<Book: {self.title} {self.desc} {self.authors}>"
    
    def print_mam(self, books_group):
        for author in books_group.authors.all():
            print (author.first_name)