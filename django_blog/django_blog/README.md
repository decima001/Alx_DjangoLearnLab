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

## Comment System
- Users can read all comments under a post.
- Only logged-in users can comment.
- Users can edit or delete their own comments.
- Comments display newest first.
- URL Structure:
  - /post/<post_id>/ → View post & comments
  - /comment/<comment_id>/edit/ → Edit comment
  - /comment/<comment_id>/delete/ → Delete comment