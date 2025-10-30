import json
from book import Book
from library import Library

def save_to_file(library, filename):
    try:
        with open(filename, 'w') as file:
            json.dump([book.__dict__ for book in library.books], file)
    except Exception as e:
        print(f"An error occurred while saving to file: {e}")

def load_from_file(filename):
    try:
        with open(filename, 'r') as file:
            books_data = json.load(file)
            library = Library()
            for data in books_data:
                library.add_book(Book(**data))
            return library
    except FileNotFoundError:
        print("File not found. Returning an empty library.")
        return Library()
    except json.JSONDecodeError:
        print("Error decoding JSON. Returning an empty library.")
        return Library()
    except Exception as e:
        print(f"An error occurred while loading from file: {e}")
        return Library()
