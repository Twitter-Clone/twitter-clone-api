from rest_framework import serializers
from tcapi.models import User, Posts, PostReactions, CommentReplies

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('userid', 
        'twitterhandle', 
        'email', 
        'password')