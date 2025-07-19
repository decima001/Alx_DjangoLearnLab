from relationship_app.models import Author, Library


def list_books_by_author(author_name):
    """
    Query all books by a specific author
    """
    try:
        author = Author.objects.get(name=author_name)
        return author.books.all()
    except Author.DoesNotExist:
        print(f"Author '{author_name}' not found.")
        return []


def list_books_in_library(library_name):
    """
    List all books in a library
    """
    library = Library.objects.get(name=library_name)
    return library.books.all()


def get_librarian_for_library(library_name):
    """
    Retrieve the librarian for a library
    """
    try:
        library = Library.objects.get(name=library_name)
        return library.librarian
    except Library.DoesNotExist:
        print(f"Library '{library_name}' not found.")
        return None
    except Exception:
        print(f"No librarian found for library '{library_name}'.")
        return None


# Example usage for testing
def run_queries():
    print("Books by Chinua Achebe:")
    for book in list_books_by_author("Chinua Achebe"):
        print(f"- {book.title}")

    print("\nBooks in National Library:")
    for book in list_books_in_library("National Library"):
        print(f"- {book.title}")

    librarian = get_librarian_for_library("National Library")
    if librarian:
        print(f"\nLibrarian: {librarian.name}")
