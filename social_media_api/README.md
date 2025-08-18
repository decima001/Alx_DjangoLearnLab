POST /posts/1/like/
{
  "detail": "Post liked."
}

GET /notifications/
[
  {
    "id": 5,
    "recipient": "alice",
    "actor": "bob",
    "verb": "liked your post",
    "target": "My First Post",
    "timestamp": "2025-08-18T19:45:12Z",
    "read": false
  }
]