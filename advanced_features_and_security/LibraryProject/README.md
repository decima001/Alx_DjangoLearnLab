# Permissions & Groups Setup in bookshelf App

## Custom Permissions (Defined in `Book` model)
- `can_view` – Allows viewing books.
- `can_create` – Allows adding new books.
- `can_edit` – Allows editing book details.
- `can_delete` – Allows deleting books.

## User Groups
- **Viewers**: `can_view`
- **Editors**: `can_view`, `can_create`, `can_edit`
- **Admins**: All permissions

## Usage
- Permissions are enforced in views using `@permission_required(...)`.
- Use the management command to set up groups:
