from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Author, Book


class BookAPITestCase(APITestCase):

    def setUp(self):
        # Create user and authenticate
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')

        # Create an author
        self.author = Author.objects.create(name='Chinua Achebe')

        # Create a book
        self.book = Book.objects.create(
            title='Things Fall Apart',
            publication_year=1958,
            author=self.author
        )

    def test_list_books(self):
        url = reverse('book-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_create_book(self):
        url = reverse('book-create')
        data = {
            "title": "A New Dawn",
            "publication_year": 2023,
            "author": self.author.id
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)

    def test_update_book(self):
        url = reverse('book-update', kwargs={'pk': self.book.pk})
        data = {
            "title": "Things Fall Apart - Revised",
            "publication_year": 1958,
            "author": self.author.id
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "Things Fall Apart - Revised")

    def test_delete_book(self):
        url = reverse('book-delete', kwargs={'pk': self.book.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(pk=self.book.pk).exists())

    def test_filter_books_by_title(self):
        url = reverse('book-list') + '?title=Things Fall Apart'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], 'Things Fall Apart')

    def test_search_books_by_title(self):
        url = reverse('book-list') + '?search=things'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(any('Things Fall Apart' in b['title'] for b in response.data))

    def test_order_books_by_year_descending(self):
        # Add another book to test ordering
        Book.objects.create(title='No Longer at Ease', publication_year=1960, author=self.author)
        url = reverse('book-list') + '?ordering=-publication_year'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        years = [b['publication_year'] for b in response.data]
        self.assertEqual(years, sorted(years, reverse=True))

    def test_unauthenticated_user_cannot_create_book(self):
        self.client.logout()
        url = reverse('book-create')
        data = {
            "title": "Forbidden",
            "publication_year": 2025,
            "author": self.author.id
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


# Test that the list endpoint returns 200 and includes at least one book