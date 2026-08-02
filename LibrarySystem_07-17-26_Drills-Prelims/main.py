# main.py - Library Book Borrowing System
# LibrarySystem_07-17-26_Drills-Prelims

from views import *

while True:

    print("\n")
    print("╔══════════════════════════════════════════════════════╗")
    print("║          📚 LIBRARY BOOK BORROWING SYSTEM 📚         ║")
    print("║          LibrarySystem_07-17-26_Drills-Prelims       ║")
    print("╠══════════════════════════════════════════════════════╣")
    print("║ 1. Show All Books                                    ║")
    print("║ 2. Borrow a Book                                     ║")
    print("║ 3. Return a Book                                     ║")
    print("║ 4. Show Available Books                              ║")
    print("║ 5. Show Borrowed Books                               ║")
    print("║ 6. Exit                                              ║")
    print("╚══════════════════════════════════════════════════════╝")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        show_all_books()

    elif choice == "2":
        borrow_book()

    elif choice == "3":
        return_book()

    elif choice == "4":
        show_available_books()

    elif choice == "5":
        show_borrowed_books()

    elif choice == "6":
        print("\n" + "=" * 60)
        print("   Thank you for using the Library Book Borrowing System!")
        print("   LibrarySystem_07-17-26_Drills-Prelims")
        print("   Have a great day! 📖")
        print("=" * 60)
        break

    else:
        print("\n❌ Invalid choice. Please enter a number from 1 to 6.")