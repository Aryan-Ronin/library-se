import unittest
from src.library import Library

class TestLibrarySprint1(unittest.TestCase):

    def test_add_book_success(self):
        lib = Library()
        lib.add_book("B1", "Python", "Guido")
        self.assertIn("B1", lib.books)

    def test_duplicate_book_raises_error(self):
        lib = Library()
        lib.add_book("B1", "Python", "Guido")
        with self.assertRaises(ValueError):
            lib.add_book("B1", "Java", "James")
            
class TestLibrarySprint2(unittest.TestCase):

    def test_borrow_book(self):
        lib = Library()
        lib.add_book("B1", "Python", "Guido")
        lib.borrow_book("B1")
        self.assertTrue(lib.books["B1"]["borrowed"])

    def test_borrow_unavailable_book(self):
        lib = Library()
        lib.add_book("B1", "Python", "Guido")
        lib.borrow_book("B1")
        with self.assertRaises(ValueError):
            lib.borrow_book("B1")

    def test_return_book(self):
        lib = Library()
        lib.add_book("B1", "Python", "Guido")
        lib.borrow_book("B1")
        lib.return_book("B1")
        self.assertFalse(lib.books["B1"]["borrowed"])
        
    class TestLibrarySprint3(unittest.TestCase):

    def test_report_has_header(self):
        lib = Library()
        report = lib.generate_report()
        self.assertIn("ID | Title | Author | Status", report)

    def test_report_has_book_entry(self):
        lib = Library()
        lib.add_book("B1", "Python", "Guido")
        report = lib.generate_report()
        self.assertIn("B1", report)



