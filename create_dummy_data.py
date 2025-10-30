import json
from book import Book
from library import Library

def create_dummy_data(filename):
    library = Library()
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

    try:
        with open(filename, 'w') as file:
            json.dump([book.__dict__ for book in library.books], file)
        print(f"Dummy data has been written to {filename}")
    except Exception as e:
        print(f"An error occurred while writing dummy data to file: {e}")

if __name__ == "__main__":
    create_dummy_data('library.json')
