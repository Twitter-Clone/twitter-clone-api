from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from django.contrib.auth.models import User
from tcapi.models import Posts, PostReactions, CommentReplies

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "email", "username")

class UserSerializerWithToken(serializers.ModelSerializer):

    token = serializers.SerializerMethodField()
    password = serializers.CharField(write_only=True)

    def get_token(self, obj):
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(obj)
        token = jwt_encode_handler(payload)
        return token

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    class Meta:
        model = User
        fields = ('token', 'username', 'password')

class PostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = ("postid", "tweet", "userid_id")


class PostReactionsSerializers(serializers.ModelSerializer):
    class Meta:
        model = PostReactions
        fields = ("reactionsid", "postlikes", "reactioncomments", "postid_id")


class CommentRepliesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentReplies
        fields = ("commentsid", "postcomments", "reactionsid_id")
