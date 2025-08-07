## API Views Documentation

### BookListView
- **URL**: `/api/books/`
- **Method**: GET
- **Access**: Public
- **Description**: Returns a list of all books.

### BookDetailView
- **URL**: `/api/books/<id>/`
- **Method**: GET
- **Access**: Public
- **Description**: Returns details of a single book.

### BookCreateView
- **URL**: `/api/books/create/`
- **Method**: POST
- **Access**: Authenticated users only
- **Description**: Creates a new book.

### BookUpdateView
- **URL**: `/api/books/<id>/update/`
- **Method**: PUT/PATCH
- **Access**: Authenticated users only
- **Description**: Updates a book.

### BookDeleteView
- **URL**: `/api/books/<id>/delete/`
- **Method**: DELETE
- **Access**: Authenticated users only
- **Description**: Deletes a book.

## API Query Features

### 🔍 Filtering
- `/api/books/?title=Things Fall Apart`
- `/api/books/?author=1`

### 🔍 Searching
- `/api/books/?search=achebe`

### 🔃 Ordering
- `/api/books/?ordering=title`
- `/api/books/?ordering=-publication_year`