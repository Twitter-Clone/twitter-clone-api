from django.db import models
from django.conf import settings

class Posts(models.Model):
    """
    Posts table
    """

    postid = models.IntegerField(blank=False, default="")
    tweet = models.CharField(max_length=280, blank=False, default="")

    # Foreign key to Users table
    userid = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class PostReactions(models.Model):
    """
    PostReactions table
    """

    reactionsid = models.IntegerField(blank=False, default="")
    postlikes = models.IntegerField(blank=False, default="")
    reactioncomments = models.CharField(max_length=280, blank=False, default="")

    # Foreign key to Posts table
    postid = models.ForeignKey(Posts, on_delete=models.CASCADE)


class CommentReplies(models.Model):
    """
    CommentReplies table
    """

    commentsid = models.IntegerField(blank=False, default="")
    postcomments = models.CharField(max_length=280, blank=False, default="")

    # Foreign key to PostReactions table
    reactionsid = models.ForeignKey(PostReactions, on_delete=models.CASCADE)
