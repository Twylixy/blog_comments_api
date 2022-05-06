from django.urls import path
from . import views
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title="Pastebin API", url="/")

urlpatterns = [
    path("docs/", schema_view),
    path("posts/", views.PostListView.as_view()),
    path("posts/<int:post_id>", views.PostDetailView.as_view()),
    path("posts/create/", views.PostCreateView.as_view()),
    path("comments/", views.CommentListView.as_view()),
    path("comments/<int:comment_id>", views.CommentDetailView.as_view()),
    path("comments/create/", views.CommentCreateView.as_view()),
    path("comments/thread/<int:head_comment_id>", views.CommentThreadView.as_view()),
]
