from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from tcapi.models import User, Posts
from tcapi.serializers import UserSerializer, PostsSerializer
from rest_framework.decorators import api_view

@api_view(['GET', 'POST', 'DELETE'])
def user_list(request):
    if request.method == 'GET':
        users = User.objects.all()
        
        twitterhandle = request.GET.get('twitterhandle', None)
        if twitterhandle is not None:
            users = users.filter(twitterhandle__icontains=twitterhandle)
        
        users_serializer = UserSerializer(users, many=True)
        return JsonResponse(users_serializer.data, safe=False)
        # 'safe=False' for objects serialization
    elif request.method == 'POST':
        user_data = JSONParser().parse(request)
        user_serializer = UserSerializer(data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse(user_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        count = User.objects.all().delete()
        return JsonResponse({'message': '{} Users were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def user_detail(request, pk):
    # find user by pk (id)
    try: 
        user = User.objects.get(pk=pk) 
    except User.DoesNotExist: 
        return JsonResponse({'message': 'The user does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    # GET / PUT / DELETE tutorial
    if request.method == 'GET':
        user_serializer = UserSerializer(user)
        return JsonResponse(user_serializer.data)

    if request.method == 'PUT':
        user_data = JSONParser().parse(request)
        user_serializer = UserSerializer(user, data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse(user_serializer.data)
        return JsonResponse(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def tweet_list(request):
    if request.method == 'GET':
        tweets = Posts.objects.all()

        tweet = request.GET.get('tweet', None)
        if tweet is not None:
            tweets = tweets.filter(tweet__icontains=tweet)

        posts_serializer = PostsSerializer(tweets, many=True)
        return JsonResponse(posts_serializer.data, safe=False)
    elif request.method == 'POST':
        tweets_data = JSONParser().parse(request)
        posts_serializer = PostsSerializer(data=tweets_data)
        if posts_serializer.is_valid():
            posts_serializer.save()
            return JsonResponse(posts_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(posts_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        count = Posts.objects.all().delete()
        return JsonResponse({'message': '{} Posts were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
