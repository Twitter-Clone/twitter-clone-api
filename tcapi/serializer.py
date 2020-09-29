"""
Import serializer for translating data.
Import all models to be translated.
"""
from rest_framework import serializers
from tcapi.models import User, Posts, PostReactions, CommentReplies

class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the User table.
    """
    class Meta:
        model = User
        fields = ('userid',
                  'twitterhandle',
                  'email',
                  'password')
"""
class PostSerializer(serializers.ModelSerializer):
    """
    #Serializer for the Post table.
    """
    class Meta:
        model = Posts
        fields = ('postid',
                  'tweet',
                  'userid')

class PostReactionsSerializers(serializers.ModelSerializer):
    """
    #Serializer for the PostReactions table.
    """
    class Meta:
        model = PostReactions
        fields = ('reactionsid',
                  'postlikes',
                  'postcomments')

class CommentRepliesSerializers(serializers.ModelSerializer):
    """
    #Serializer for the CommentReplies table.
    """
    class Meta:
        model = CommentReplies
        fields = ('commentsid',
                  'postcomments')
"""
