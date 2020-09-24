```
TODO: documentation
```
from django.db import models

<<<<<<< HEAD

class Users(models.Model):
    ```
    Users Table
    ```
    userid = models.IntegerField(max_length=8, blank=False, default='')
    twitterhandle = models.CharField(max_length=15, blank=False, default='')
    email = models.EmailField(max_length=254, blank=False, default='')
    password = CharField(max_length=128, blank=False, default='') 

class Posts(models.Model):
    ```
    Posts Table
    ```
    postid = models.IntegerField(max_length=8, blank=False, default='')
    tweet = models.CharField(max_length=280, blank=False, default='')
        
    # Foreign key to Users table
    userid = models.ForeignKey(Users, on_delete=models.CASCADE)

class PostReactions(models.model):
    ```
    PostsReactions
    ```
    reactionsid = models.IntegerField(max_length=8, blank=False, default='')
    postlikes = models.IntegerField(max_length=8, blank=False, default='') 
    postcomments = models.CharField(max_length=280, blank=False, default='') 
    
    # Foreign key to Posts table
    postid = models.ForeignKey(Posts, on_delete=models.CASCASE)

class CommentReplies(models.Model):
    ```
    CommentReplies Table
    ```
    commentsid = models.IntegerField(max_length=8, blank=False, default='')
    postcomments = models.CharField(max_length=280, blank=False, default='')

    # Foreign key to PostReactions table
    reactionsid = models.ForeignKey(PostReactions, on_delete=models.CASCADE)
    
=======
class Tcapi(models.Model):
  
>>>>>>> ae92381c8cdabfe2996fc2999f869b025269e99a
