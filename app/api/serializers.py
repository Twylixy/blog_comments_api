from .models import Post, Comment
from rest_framework import serializers


class FilterParentCommentSerializer(serializers.ListSerializer):
    """Filter only parent comment"""

    def to_representation(self, data):
        data = data.filter(reply_to=None)
        return super().to_representation(data)


class StrictedRecursiveChildCommentSerializer(serializers.Serializer):
    """Get all child comments"""

    def to_representation(self, comment: Comment):
        if comment.nesting_level > 3:
            return None
        serializer = self.parent.parent.__class__(comment, context=self.context)
        return serializer.data


class RecursiveChildCommentSerializer(serializers.Serializer):
    """Get all child comments withot nesting level"""

    def to_representation(self, comment: Comment):
        serializer = self.parent.parent.__class__(comment, context=self.context)
        return serializer.data


class CommentSerializer(serializers.ModelSerializer):
    """Comment serializer with replies"""

    replies = RecursiveChildCommentSerializer(many=True)

    class Meta:
        list_serializer_class = FilterParentCommentSerializer
        model = Comment
        fields = ("id", "author", "text", "reply_to", "replies")


class ChildCommentSerializer(serializers.ModelSerializer):
    """Child comment serializer"""

    replies = StrictedRecursiveChildCommentSerializer(many=True)

    class Meta:
        model = Comment
        fields = ("id", "author", "text", "reply_to", "replies")


class PostListSerializer(serializers.ModelSerializer):
    """Post list serializer"""

    class Meta:
        model = Post
        fields = ("id", "author", "created_at", "content")


class PostCreateSerializer(serializers.ModelSerializer):
    """Post create serializer"""

    class Meta:
        model = Post
        fields = ("author_id", "author", "content")


class PostDetailSerializer(serializers.ModelSerializer):
    """Post detail serializer"""

    comments = CommentSerializer(many=True)

    class Meta:
        model = Post
        fields = "__all__"


class CommentListSerializer(serializers.ModelSerializer):
    """Comment list serializer"""

    class Meta:
        model = Comment
        fields = ("id", "author_id", "created_at", "post_id", "text")


class CommentCreateSerializer(serializers.ModelSerializer):
    """Comment create serializer"""

    class Meta:
        model = Comment
        fields = ("author_id", "author", "text", "reply_to", "post")


class CommentDetailSerializer(serializers.ModelSerializer):
    """Comment detail serializer"""

    class Meta:
        model = Comment
        fields = "__all__"


class CommentThreadSerializer(serializers.ModelSerializer):
    """Thread of comments serializer"""

    replies = ChildCommentSerializer(many=True)

    class Meta:
        model = Comment
        fields = "__all__"
