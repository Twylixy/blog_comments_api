from django.db import models
from datetime import datetime


class Post(models.Model):
    author_id = models.IntegerField(null=False, blank=False)
    author = models.CharField(max_length=64, null=False, blank=False)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    modified_at = models.DateTimeField(null=True, blank=True)
    content = models.TextField()


class Comment(models.Model):
    author_id = models.IntegerField(null=False, blank=False)
    author = models.CharField(max_length=64, null=False, blank=False)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    modified_at = models.DateField(null=True, blank=True)
    reply_to = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="replies",
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="comments",
    )
    text = models.TextField()
    nesting_level = models.IntegerField(default=0, blank=True, null=True)
