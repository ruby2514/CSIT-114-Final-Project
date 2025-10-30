from book import Book
from library import Library
import file_operations

def create_dummy_data(library):
    dummy_books = [
        Book("The Great Gatsby", "F. Scott Fitzgerald", 1925, "9780743273565"),
        Book("To Kill a Mockingbird", "Harper Lee", 1960, "9780061120084"),
        Book("1984", "George Orwell", 1949, "9780451524935"),
        Book("Pride and Prejudice", "Jane Austen", 1813, "9781503290563"),
        Book("The Catcher in the Rye", "J.D. Salinger", 1951, "9780316769488"),
        Book("Moby Dick", "Herman Melville", 1851, "9781503280786"),
        Book("War and Peace", "Leo Tolstoy", 1869, "9781400079988"),
        Book("The Odyssey", "Homer", -800, "9780140268867"),
        Book("The Divine Comedy", "Dante Alighieri", 1320, "9780142437223"),
        Book("Hamlet", "William Shakespeare", 1603, "9780743477123"),
        Book("The Hobbit", "J.R.R. Tolkien", 1937, "9780547928227"),
        Book("Crime and Punishment", "Fyodor Dostoevsky", 1866, "9780486415871")
    ]

    for book in dummy_books:
        library.add_book(book)

    print("Dummy data has been added to the library.")

def main():
    library = file_operations.load_from_file('library.json')

    while True:
        print("\nLibrary Menu:")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. View Books")
        print("4. Save and Exit")
        print("5. Create Dummy Data")
        choice = input("Choose an option: ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            year = input("Enter book year: ")
            isbn = input("Enter book ISBN: ")
            try:
                book = Book(title, author, int(year), isbn)
                library.add_book(book)
            except ValueError:
                print("Invalid year. Please enter a valid number.")
        elif choice == '2':
            isbn = input("Enter book ISBN to remove: ")
            if library.remove_book(isbn):
                print("Book removed successfully.")
            else:
                print("Book not found.")
        elif choice == '3':
            for book in library.view_books():
                print(book)
        elif choice == '4':
            file_operations.save_to_file(library, 'library.json')
            print("Library saved. Exiting.")
            break
        elif choice == '5':
            create_dummy_data(library)
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
