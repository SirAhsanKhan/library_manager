import json
import os

# File to store the library data
LIBRARY_FILE = "library.json"

# Initialize the library as an empty list
library = []

# Load library from file if it exists
def load_library():
    global library
    if os.path.exists(LIBRARY_FILE):
        with open(LIBRARY_FILE, "r") as file:
            library = json.load(file)

# Save library to file
def save_library():
    with open(LIBRARY_FILE, "w") as file:
        json.dump(library, file, indent=4)

# Add a book to the library
def add_book():
    title = input("Enter the title: ")
    author = input("Enter the author: ")
    year = int(input("Enter the publication year: "))
    genre = input("Enter the genre: ")
    read_status = input("Have you read this book? (yes/no): ").lower() == "yes"

    book = {
        "title": title,
        "author": author,
        "publication_year": year,
        "genre": genre,
        "read_status": read_status
    }
    library.append(book)
    print(f"Book '{title}' added successfully!")
    save_library()

# Remove a book from the library
def remove_book():
    title = input("Enter the title of the book to remove: ")
    global library
    library = [book for book in library if book["title"].lower() != title.lower()]
    print(f"Book '{title}' removed successfully!")
    save_library()

# Search for a book by title or author
def search_book():
    search_term = input("Enter the title or author to search: ").lower()
    results = [book for book in library if search_term in book["title"].lower() or search_term in book["author"].lower()]
    
    if results:
        print("\nSearch Results:")
        for book in results:
            print(f"Title: {book['title']}, Author: {book['author']}, Year: {book['publication_year']}, Genre: {book['genre']}, Read: {'Yes' if book['read_status'] else 'No'}")
    else:
        print("No matching books found.")

# Display all books in the library
def display_all_books():
    if not library:
        print("The library is empty.")
    else:
        print("\nAll Books:")
        for book in library:
            print(f"Title: {book['title']}, Author: {book['author']}, Year: {book['publication_year']}, Genre: {book['genre']}, Read: {'Yes' if book['read_status'] else 'No'}")

# Display library statistics
def display_statistics():
    total_books = len(library)
    read_books = sum(book["read_status"] for book in library)
    percentage_read = (read_books / total_books * 100) if total_books > 0 else 0

    print("\nLibrary Statistics:")
    print(f"Total Books: {total_books}")
    print(f"Percentage Read: {percentage_read:.2f}%")

# Main menu
def main_menu():
    while True:
        print("\nPersonal Library Manager")
        print("1. Add a Book")
        print("2. Remove a Book")
        print("3. Search for a Book")
        print("4. Display All Books")
        print("5. Display Statistics")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            remove_book()
        elif choice == "3":
            search_book()
        elif choice == "4":
            display_all_books()
        elif choice == "5":
            display_statistics()
        elif choice == "6":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Entry point of the program
if __name__ == "__main__":
    load_library()
    main_menu()