# data.py - Book data management
# LibrarySystem_07-17-26_Drills-Prelims

class Library:
    def __init__(self):
        self.books = [
            {"title": "Noli Me Tangere", "author": "Jose Rizal", "is_borrowed": False},
            {"title": "El Filibusterismo", "author": "Jose Rizal", "is_borrowed": False},
            {"title": "Florante at Laura", "author": "Francisco Balagtas", "is_borrowed": True},
            {"title": "Ibong Adarna", "author": "Unknown", "is_borrowed": False},
            {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "is_borrowed": False},
            {"title": "To Kill a Mockingbird", "author": "Harper Lee", "is_borrowed": True},
            {"title": "1984", "author": "George Orwell", "is_borrowed": False},
            {"title": "Pride and Prejudice", "author": "Jane Austen", "is_borrowed": False},
        ]
    
    def get_all_books(self):
        return self.books
    
    def get_available_books(self):
        return [book for book in self.books if not book["is_borrowed"]]
    
    def get_borrowed_books(self):
        return [book for book in self.books if book["is_borrowed"]]
    
    def borrow_book_by_index(self, index):
        available = self.get_available_books()
        if 0 <= index < len(available):
            available[index]["is_borrowed"] = True
            return True
        return False
    
    def return_book_by_index(self, index):
        borrowed = self.get_borrowed_books()
        if 0 <= index < len(borrowed):
            borrowed[index]["is_borrowed"] = False
            return True
        return False