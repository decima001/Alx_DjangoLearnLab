from relationship_app.models import Author, Library

def list_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        return library.books.all()
    except Library.DoesNotExist:
        print("Library not found.")
        return []

def run_queries():
    # 1. Query all books by a specific author
    try:
        author = Author.objects.get(name="Chinua Achebe")
        books = author.books.all()
        print(f"Books by {author.name}:")
        for book in books:
            print(book.title)
    except Author.DoesNotExist:
        print("Author not found.")

    # 2. List all books in a library
    try:
        library = Library.objects.get(name="National Library")
        print(f"Books in {library.name}:")
        for book in library.books.all():
            print(book.title)
    except Library.DoesNotExist:
        print("Library not found.")

    # 3. Retrieve the librarian for a library
    try:
        librarian = library.librarian  # using reverse relation
        print(f"Librarian of {library.name}: {librarian.name}")
    except AttributeError:
        print("No librarian assigned to this library.")
