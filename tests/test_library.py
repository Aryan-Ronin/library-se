import unittest
from src.library import Library

class TestSprint1(unittest.TestCase):

    def test_add_book_success(self):
        lib = Library()
        lib.add_book("B1", "Python", "Guido")
        self.assertIn("B1", lib.books)

    def test_duplicate_book_raises_error(self):
        lib = Library()
        lib.add_book("B1", "Python", "Guido")
        with self.assertRaises(ValueError):
            lib.add_book("B1", "Java", "James")
class TestSprint2(unittest.TestCase):

    def test_borrow_available_book(self):
        lib = Library()
        lib.add_book("B1", "Python", "Guido")
        lib.borrow_book("B1")
        self.assertTrue(lib.books["B1"]["borrowed"])

    def test_borrow_unavailable_book_raises_error(self):
        lib = Library()
        lib.add_book("B1", "Python", "Guido")
        lib.borrow_book("B1")
        with self.assertRaises(ValueError):
            lib.borrow_book("B1")

    def test_return_book_updates_status(self):
        lib = Library()
        lib.add_book("B1", "Python", "Guido")
        lib.borrow_book("B1")
        lib.return_book("B1")
        self.assertFalse(lib.books["B1"]["borrowed"])
