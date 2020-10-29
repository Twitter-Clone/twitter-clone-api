from django.db import models


# Create your models here.
class User(models.Model):
    """
    Users table
    """

    userid = models.IntegerField(blank=False, default="")
    twitterhandle = models.CharField(max_length=15, blank=False, default="")
    email = models.EmailField(max_length=254, blank=False, default="")
    password = models.CharField(max_length=128, blank=False, default="")


class Posts(models.Model):
    """
    Posts table
    """

    postid = models.IntegerField(blank=False, default="")
    tweet = models.CharField(max_length=280, blank=False, default="")

    # Foreign key to Users table
    userid = models.ForeignKey(User, on_delete=models.CASCADE)


class PostReactions(models.Model):
    """
    PostReactions table
    """

    reactionsid = models.IntegerField(blank=False, default="")
    postlikes = models.IntegerField(blank=False, default="")
    postcomments = models.CharField(max_length=280, blank=False, default="")

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
