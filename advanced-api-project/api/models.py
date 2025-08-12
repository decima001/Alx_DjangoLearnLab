from django.db import models

# The Author model stores basic information about a book author.
class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

# The Book model stores information on books, including a foreign key to the author.
class Book(models.Model):
    title = models.CharField(max_length=255)
    publication_year = models.PositiveIntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
# Create your models here.
