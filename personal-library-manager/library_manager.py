import json
import os

data_file = 'library.txt'

def load_library():
    if os.path.exists(data_file):
        with open(data_file,'r') as file:
            return json.load(file)
        return []
    
def save_library(library):
    with open(data_file, 'w') as file:
        json.dump(library, file)

def add_book(library):
    title = input("Enter book title: ")
    author = input('Enter book author: ')
    year = input('Enter book year: ')
    genre = input('Enter book genre: ')
    read = input('Have you read this book? (yes/no): ').lower() == 'yes'

    new_book = {
        'title': title,
        'author': author,
        'year': year,
        'genre': genre,
        'read': read
    }

    library.append(new_book)
    save_library(library)
    print(f"Book {title} added to the library.")

def remove_book(library):
    title = input("Enter the title of the book to remove: ")
    inititial_length = len(library)
    library = [book for book in library if book['title'].lower() != title]
    if len(library) < inititial_length:
        save_library(library)
        print(f"Book {title} removed from the library.")
    else:
        print(f"Book {title} not found in the library.")

def search_library(library):
    search_by = input("Search by title or author: ").lower()
    search_term = input(f"Enter  {search_by} to search for: ").lower()

    results = [book for book in library if search_term in book[search_by].lower()]

    if results:
        for book in results:
            status = "Read" if book['read'] else "UnRead"
            print(f"{book['title']} by {book['author']} - {book['year']} - {book['genre']} - {status}")
    else:
        print(f"No books found matching {search_term} in the {search_by} field.")

def display_all_books(library):
    if library:
        for book in library:
            status = "Read" if book['read'] else "UnRead"
            print(f"{book['title']} by {book['author']} - {book['year']} - {book['genre']} - {status}")
    else:
        print("No books in the library.")


def display_statistics(library):
    total_books = len(library)
    read_books = len([book for book in library if book['read']])
    percentage_read = (read_books / total_books) * 100 if total_books > 0 else 0

    print(f'Total books: {total_books}')
    print(f'Percentage of books read: {percentage_read:.2f}%')


def main():
    library = load_library()
    while True:
        print("Welcome to your Personal Library Manager")
        print("Menu")
        print("1. Add a Book")
        print("2. Remove a Book")
        print("3. Search Library")
        print("4. Display All Books")
        print("5. Display Statistics")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_book(library)
        elif choice == '2':
            remove_book(library)
        elif choice == '3':
            search_library(library)
        elif choice == '4':
            display_all_books(library)
        elif choice == '5':
            display_statistics(library)
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")    

if __name__ == "__main__":
    main()
    