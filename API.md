# Project's API

* /api/v1
  * /docs - Swagger documentation.
  * /posts - GET-method for all posts.
    * /create - POST-method for creating a new post.
    * /\<post_id\> - GET-method for get details about post.
  * /comments - GET-method for all comments.
    * /create - POST-method for creating a new comment.
    * /\<comment_id\> - GET-method for get details about comment.
    * /thread/\<comment_id> - GET-method for all replies for comment with specified id

**Payload scheme for /api/v1/comments/create**
```JSON
{
  "author_id": int (Required),
  "author": str (Required),
  "created_at": datetime (Optional),
  "modified_at": datetime (Optional),
  "reply_to": int (Optional),
  "post": int (Required),
  "text": str (Required)
}
```

**Payload scheme for /api/v1/posts/create**
```JSON
{
  "author_id": int (Required),
  "author": str (Required),
  "created_at": datetime (Optional),
  "modified_at": datetime (Optional),
  "content": str (Required)
}
```

Note: /api/v1/comments/thread/\<comment_id\> will show tree of comments from \<comment_id\>.