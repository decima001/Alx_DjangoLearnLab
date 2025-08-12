## Blog Post Management Features

### Views:
- ListView: `/` → All posts
- DetailView: `/posts/<id>/` → Post details
- CreateView: `/posts/new/` → Create new post
- UpdateView: `/posts/<id>/edit/` → Edit post (author only)
- DeleteView: `/posts/<id>/delete/` → Delete post (author only)

### Permissions:
- Any user can view posts
- Only authenticated users can create posts
- Only authors can edit/delete their posts