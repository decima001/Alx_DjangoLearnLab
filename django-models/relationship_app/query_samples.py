from relationship_app.models import Author, Library

def list_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.books.all()

def run_queries():
    
    try:
        author = Author.objects.get(name="Chinua Achebe")
        books = author.books.all()
        print(f"Books by {author.name}:")
        for book in books:
            print(book.title)
    except Author.DoesNotExist:
        print("Author not found.")

def run_queries():
    
    try:
        library_name = "National Library"
        books = list_books_in_library(library_name)
        print(f"Books in {library_name}:")
        for book in books:
            print(book.title)
    except Library.DoesNotExist:
        print("Library not found.")

    try:
        library = Library.objects.get(name="National Library")
        librarian = library.librarian
        print(f"Librarian of {library.name}: {librarian.name}")
    except Library.DoesNotExist:
        print("Library not found.")
    except Exception:
        print("No librarian found.")

