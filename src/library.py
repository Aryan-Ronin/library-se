class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, book_id, title, author):
        if book_id in self.books:
            raise ValueError("Duplicate Book ID")
        self.books[book_id] = {
            "title": title,
            "author": author,
            "borrowed": False
        }
        def borrow_book(self, book_id):
        if self.books[book_id]["borrowed"]:
            raise ValueError("Book already borrowed")
        self.books[book_id]["borrowed"] = True

    def return_book(self, book_id):
        self.books[book_id]["borrowed"] = False
        
   def generate_report(self):
        report = "ID | Title | Author | Status\n"
        for bid, b in self.books.items():
            status = "Borrowed" if b["borrowed"] else "Available"
            report += f"{bid} | {b['title']} | {b['author']} | {status}\n"
        return report


