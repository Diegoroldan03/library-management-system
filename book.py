class Book:
    """Represent a book in the library"""

    def __init__(self, title, author, isbn):
        """
        Initialize a new Book object.
        Parameters:
            title (str): The title of the book.
            author (str): The author of the book.
            isbn (str): The ISBN of the book.
        """
        self.title = title
        self.author = author
        self. isbn = isbn

    def __str__(self):
        """
        Format the book information for display.
        Returns:
            str: The title, author, and ISBN of the book.
        """
        return (
            f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}"
        )
    def get_details(self):
        """
        Provide all stored details for the book.
        Returns:
            dict: The title, author, and ISBN
        """
        return {
            "Title": self.title,
            "Author": self.author,
            "ISBN": self.isbn
        }