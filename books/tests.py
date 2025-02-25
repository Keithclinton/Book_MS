from django.test import TestCase
from .models import Book
from datetime import date

class BookModelTest(TestCase):
    def setUp(self):
        Book.objects.create(
            title="Test Book",
            author="John Doe",
            publication_date=date(2020, 1, 1),
            isbn="1234567890",
            summary="This is a test book."
        )

    def test_book_creation(self):
        book = Book.objects.get(title="Test Book")
        self.assertEqual(book.author, "John Doe")
        self.assertEqual(book.isbn, "1234567890")

class BookAPITest(TestCase):
    def setUp(self):
        self.book_data = {
            "title": "New Book",
            "author": "Jane Doe",
            "publication_date": "2019-05-15",
            "isbn": "9876543210123",
            "summary": "This is another test book."
        }

    def test_create_book(self):
        response = self.client.post('/api/books/', self.book_data, content_type="application/json")
        self.assertEqual(response.status_code, 201)
