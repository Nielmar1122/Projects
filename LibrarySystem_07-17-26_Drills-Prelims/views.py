# views.py - All display and logic functions for the Library System
# LibrarySystem_07-17-26_Drills-Prelims

# Sample book data (title, author, is_borrowed)
books = [
    {"title": "Noli Me Tangere", "author": "Jose Rizal", "is_borrowed": False},
    {"title": "El Filibusterismo", "author": "Jose Rizal", "is_borrowed": False},
    {"title": "Florante at Laura", "author": "Francisco Balagtas", "is_borrowed": True},
    {"title": "Ibong Adarna", "author": "Unknown", "is_borrowed": False},
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "is_borrowed": False},
    {"title": "To Kill a Mockingbird", "author": "Harper Lee", "is_borrowed": True},
    {"title": "1984", "author": "George Orwell", "is_borrowed": False},
    {"title": "Pride and Prejudice", "author": "Jane Austen", "is_borrowed": False},
]

def show_all_books():
    """Display all books in the library"""
    print("\n" + "=" * 60)
    print("   ALL BOOKS IN THE LIBRARY")
    print("=" * 60)
    
    if not books:
        print("   No books available in the library.")
        return
    
    for i, book in enumerate(books, start=1):
        status = "❌ BORROWED" if book["is_borrowed"] else "✅ AVAILABLE"
        print(f"{i}. {book['title']} by {book['author']} - {status}")
    
    print(f"\nTotal books: {len(books)}")
    print("=" * 60)

def show_available_books():
    """Display all available books"""
    print("\n" + "=" * 60)
    print("   AVAILABLE BOOKS")
    print("=" * 60)
    
    available = [book for book in books if not book["is_borrowed"]]
    
    if not available:
        print("   No books available at the moment.")
        return
    
    for i, book in enumerate(available, start=1):
        print(f"{i}. {book['title']} by {book['author']}")
    
    print(f"\nTotal available books: {len(available)}")
    print("=" * 60)

def show_borrowed_books():
    """Display all borrowed books"""
    print("\n" + "=" * 60)
    print("   BORROWED BOOKS")
    print("=" * 60)
    
    borrowed = [book for book in books if book["is_borrowed"]]
    
    if not borrowed:
        print("   No books are currently borrowed.")
        return
    
    for i, book in enumerate(borrowed, start=1):
        print(f"{i}. {book['title']} by {book['author']}")
    
    print(f"\nTotal borrowed books: {len(borrowed)}")
    print("=" * 60)

def borrow_book():
    """Borrow a book from the library"""
    print("\n" + "=" * 60)
    print("   BORROW A BOOK")
    print("=" * 60)
    
    # Show available books first
    available = [book for book in books if not book["is_borrowed"]]
    
    if not available:
        print("   ❌ No books available to borrow.")
        return
    
    print("\nAvailable books:")
    for i, book in enumerate(available, start=1):
        print(f"{i}. {book['title']} by {book['author']}")
    
    try:
        choice = int(input("\nEnter the number of the book to borrow: "))
        if 1 <= choice <= len(available):
            selected_book = available[choice - 1]
            selected_book["is_borrowed"] = True
            print(f"\n✅ You have successfully borrowed '{selected_book['title']}'!")
            print("   Please return it on time.")
        else:
            print("\n❌ Invalid book number.")
    except ValueError:
        print("\n❌ Please enter a valid number.")

def return_book():
    """Return a borrowed book"""
    print("\n" + "=" * 60)
    print("   RETURN A BOOK")
    print("=" * 60)
    
    # Show borrowed books first
    borrowed = [book for book in books if book["is_borrowed"]]
    
    if not borrowed:
        print("   No books are currently borrowed.")
        return
    
    print("\nBorrowed books:")
    for i, book in enumerate(borrowed, start=1):
        print(f"{i}. {book['title']} by {book['author']}")
    
    try:
        choice = int(input("\nEnter the number of the book to return: "))
        if 1 <= choice <= len(borrowed):
            selected_book = borrowed[choice - 1]
            selected_book["is_borrowed"] = False
            print(f"\n✅ You have successfully returned '{selected_book['title']}'!")
            print("   Thank you!")
        else:
            print("\n❌ Invalid book number.")
    except ValueError:
        print("\n❌ Please enter a valid number.")