from rest_framework import serializers
from tcapi.models import User, Posts, PostReactions, CommentReplies


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('userid',
                  'twitterhandle',
                  'email',
                  'password')


class PostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = ('postid',
                  'tweet',
                  'userid_id')


class PostReactionsSerializers(serializers.Model):
    class Meta:
        model = PostReactions
        fields = ('reactionsid',
                  'postlikes',
                  'postcomments',
                  'postid_id')


class CommentRepliesSerializers(serializers.Model):
    class Meta:
        model = CommentReplies
        fields = ('commentsid',
                  'postcomments',
                  'reactionsid_id')
