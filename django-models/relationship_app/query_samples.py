from relationship_app.models import Author, Library

def list_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.books.all()

def run_queries():
    # Example usage of the list_books_in_library function
    try:
        library_name = "National Library"
        books = list_books_in_library(library_name)
        print(f"Books in {library_name}:")
        for book in books:
            print(book.title)
    except Library.DoesNotExist:
        print("Library not found.")
