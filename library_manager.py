# Import the Book class form book.py
from book import Book

# Add a new book to the library
def add_book(library):
    """
    Collect book information and store a new Book object.

    Parameters:
    library (list): The list used to store Book objects.

    Returns: None
    """

    # Ask the user for the book information
    title = input("Enter the book title")
    author = input("Enter the book author")
    isbn = input("Enter the book ISBN")

    # Create a new Book object
    new_book = Book(title, author, isbn)

    #Add the Book object to the library list
    library.append(new_book)

    print("Book added successfully")

# Display all books in the library
def list_books(library):
    """
    Display all the books stored in the library.

    Parameters:
    library (list): The list containing the Book objects.

    Returns: None
    """

    # Check if the library has o books
    if not library:
        print("The library is empty.")
        return
    print("\nBooks in the library:")

    # Print each Book object
    for book in library:
        print(book)

# Search for a book by title or author
def find_book(library, query):
    """
    Search for a book by its title or author.

    Parameters:
    library (list): The list containing the Book objects.

    query (str): The title or author used for the search.

    Returns: Book or None: The matching book, or None if it isn't found.
    """

    # Convert the search to lowercase
    query = query.lower()

    # Compare the search with each book
    for book in library:
        if query in book.title.lower() or query in book.author.lower():
            return book

    # Return name if no book matches the search
    return None

#Run the main program
def main():
   """
    Run the library management menu.

    Returns: None
    """

# Create an empty  list to store Book objects
my_library = []

# Keep showing the menu until the user exits
while True:
    print("\nLibrary Management System")
    print("1. Add a new book")
    print("2. List all books")
    print("3. Find a book")
    print("4. Exit the program")

    # Ask the user to select a menu option
    choice = input("Choose an option")

    # Option 1: Add a book
    if choice == "1":
        add_book(my_library)

    # Option 2: List all books
    elif choice == "2":
        list_books(my_library)

    # Option 3: FInd a book
    elif choice == "3":
        query = input("Enter a title or author: ")
        found_book = find_book(my_library, query)

        if found_book:
            print("Book found:")
            print(found_book)
        else:
            print("Book not found")
    # Option 4: Exit the program
    elif choice == "4":
        print("Thank you for using the librery system!")
        break

    # Handle an invalid menu option
    else:
        print("Invalid option, Please choose from 1 to 4.")

# Run the main() only when this file is executed directly
if __name__ == "__main__":
    main()
