# relationship_app/query_samples.py

from relationship_app.models import Author, Book, Library, Librarian

def run_queries():
    # 1. Query all books by a specific author
    author_name = "Chinua Achebe"
    try:
        author = Author.objects.get(name=author_name)
        books_by_author = author.books.all()
        print(f"Books by {author.name}:")
        for book in books_by_author:
            print(f"- {book.title}")
    except Author.DoesNotExist:
        print(f"No author named '{author_name}' found.")

    # 2. List all books in a library
    library_name = "Central Library"
    try:
        library = Library.objects.get(name=library_name)
        books_in_library = library.books.all()
        print(f"\nBooks in {library.name}:")
        for book in books_in_library:
            print(f"- {book.title}")
    except Library.DoesNotExist:
        print(f"No library named '{library_name}' found.")

    # 3. Retrieve the librarian for a library
    try:
        librarian = library.librarian
        print(f"\nLibrarian of {library.name}: {librarian.name}")
    except Exception:
        print(f"No librarian assigned to {library.name}.")

# Only run if this script is executed directly
if __name__ == "__main__":
    run_queries()