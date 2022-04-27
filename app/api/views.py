from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from .models import Post, Comment
from .serializers import (
    PostDetailSerializer,
    PostListSerializer,
    CommentListSerializer,
    PostCreateSerializer,
    CommentCreateSerializer,
    CommentDetailSerializer,
    CommentThreadSerializer,
)



class PostListView(APIView):
    """Get list of posts"""

    def get(self, request):
        posts = Post.objects.all()
        serializer = PostListSerializer(posts, many=True)
        return Response(serializer.data, status=200)


class PostCreateView(APIView):
    """Create a post"""

    def post(self, request):
        post_ = PostCreateSerializer(data=request.data)

        if not post_.is_valid():
            return Response(status=400)

        post_.save()
        return Response(status=201)


class PostDetailView(APIView):
    """Get post details"""

    def get(self, request, post_id):
        post = Post.objects.get(id=post_id)
        serializer = PostDetailSerializer(post)
        return Response(serializer.data, status=200)


class CommentListView(APIView):
    """Get list of comments"""

    def get(self, request):
        comments = Comment.objects.all()
        serializer = CommentListSerializer(comments, many=True)
        return Response(serializer.data, status=200)


class CommentCreateView(APIView):
    """Create a comment"""

    def post(self, request):
        if "reply_to" in request.data:
            repliable_comment = Comment.objects.get(id=request.data["reply_to"])
            request.data.update({"nesting_level": repliable_comment.nesting_level + 1})

        comment = CommentCreateSerializer(data=request.data)

        if not comment.is_valid():
            return Response(status=400)

        comment.save()
        return Response(status=201)


class CommentDetailView(APIView):
    """Get comment details"""

    def get(self, request, comment_id):
        comment = Comment.objects.get(id=comment_id)
        serializer = CommentDetailSerializer(comment)
        return Response(serializer.data, status=200)


class CommentThreadView(APIView):
    """Get thread from head comment"""

    def get(self, request, head_comment_id):
        comment = Comment.objects.get(id=head_comment_id)
        serializer = CommentThreadSerializer(comment)
        return Response(serializer.data, status=200)



