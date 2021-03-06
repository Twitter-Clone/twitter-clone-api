"""
TODO: Import documentation
"""
from django.test import TestCase
from tcapi.models import User, Posts #, PostReactions, CommentReplies
from django.test.client import Client


class StatusTests(TestCase):
    """
    This class tests that a connection is made to our API.
    """

    def setUp(self):
        self.client = Client()

    def test_users_endpoint(self):
        """
        GET request to our api returning a 200 status code.
        """
        response = self.client.get("/api/users")
        self.assertEqual(response.status_code, 200)

    def test_posts_endpoint(self):
        """
        GET request to our api returning a 200 status code.
        """
        response = self.client.get("/api/posts")
        self.assertEqual(response.status_code, 200)


class UserTableTests(TestCase):
    """
    These set of tests checks various areas related to the User's table.
    """

    def test_add_user(self):
        """
        Adds a new user to the database
        """
        User.objects.create(
            userid="9876543",
            twitterhandle="test1",
            email="test1@test.com",
            password="PASSWORD",
        )

        num_users = User.objects.count()

        self.assertEqual(num_users, 1)

    def test_add_users(self):
        """
        Adds multiple users to the database
        """
        User.objects.create(
            userid="1357924",
            twitterhandle="test1",
            email="test1@test.com",
            password="PASSWORD",
        )
        User.objects.create(
            userid="9876543",
            twitterhandle="test2",
            email="test2@test.com",
            password="PASSWORD",
        )
        User.objects.create(
            userid="1234567",
            twitterhandle="test3",
            email="test3@test.com",
            password="PASSWORD",
        )

        num_users = User.objects.count()

        self.assertEqual(num_users, 3)

    def test_get_all(self):
        """
        Get all users from the database.
        """
        twitterhandle = User.objects.all()

        self.assertEqual(len(twitterhandle), 3)

        # self.assertEqual(twitterhandle.status_code, 302)

        return str(twitterhandle)

    def test_get_user(self):
        """
        Given an email address, return a twitterhandle.
        """
        user = User.objects.create(
            userid="9876543",
            twitterhandle="test1",
            email="test1@test.com",
            password="PASSWORD",
        )

        twitterhandle = User.objects.get(twitterhandle="test1")

        self.assertEqual(twitterhandle, user)

        return str(twitterhandle)

    def test_get_users(self):
        """
        Gets two users from the database
        """
        user = User.objects.create(
            userid="9876543",
            twitterhandle="test1",
            email="test1@test.com",
            password="PASSWORD",
        )
        user2 = User.objects.create(
            userid="9879874",
            twitterhandle="test2",
            email="test2@test.com",
            password="PASSWORD",
        )

        twitterhandle1 = User.objects.get(email="test1@test.com")
        twitterhandle2 = User.objects.get(email="test2@test.com")

        self.assertEqual(twitterhandle1, user)
        self.assertEqual(twitterhandle2, user2)

    def test_delete_users(self):
        """
        Creates and deletes all users from the database
        """
        User.objects.create(
            userid="337282",
            twitterhandle="test1",
            email="test1@test.com",
            password="PASSWORD",
        )
        User.objects.create(
            userid="1325110",
            twitterhandle="test2",
            email="test2@test.com",
            password="PASSWORD",
        )
        User.objects.create(
            userid="5230033",
            twitterhandle="test3",
            email="test3@test.com",
            password="PASSWORD",
        )
        User.objects.create(
            userid="1000073",
            twitterhandle="test4",
            email="test4@test.com",
            password="PASSWORD",
        )

        User.objects.all().delete()

        num_users = User.objects.count()

        self.assertEqual(num_users, 0)

    def test_delete_user(self):
        """
        Creates and deletes one user from the database
        """
        User.objects.create(
            userid="337282",
            twitterhandle="test1",
            email="test1@test.com",
            password="PASSWORD",
        )
        User.objects.create(
            userid="1325110",
            twitterhandle="test2",
            email="test2@test.com",
            password="PASSWORD",
        )
        User.objects.create(
            userid="5230033",
            twitterhandle="test3",
            email="test3@test.com",
            password="PASSWORD",
        )
        User.objects.create(
            userid="1000073",
            twitterhandle="test4",
            email="test4@test.com",
            password="PASSWORD",
        )

        User.objects.get(twitterhandle="test1").delete()
        num_users = User.objects.count()
        self.assertEqual(num_users, 3)

    def test_update_user(self):
        """
        Creates and updates the email of one user from the database
        """
        User.objects.create(
            userid="337282",
            twitterhandle="test1",
            email="test1@test.com",
            password="PASSWORD",
        )
        User.objects.create(
            userid="1325110",
            twitterhandle="test2",
            email="test2@test.com",
            password="PASSWORD",
        )
        User.objects.create(
            userid="5230033",
            twitterhandle="test3",
            email="test3@test.com",
            password="PASSWORD",
        )
        User.objects.create(
            userid="1000073",
            twitterhandle="test4",
            email="test4@test.com",
            password="PASSWORD",
        )

        new_object = User.objects.get(twitterhandle="test2")
        new_object.email = "myemail2test@hotmail.com"
        new_object.save()

        response = User.objects.get(twitterhandle="test2")

        self.assertEqual(response.email, "myemail2test@hotmail.com")

    def test_update_users(self):
        """
        Creates and updates the email of two users from the database
        """
        User.objects.create(
            userid="337282",
            twitterhandle="test1",
            email="test1@test.com",
            password="PASSWORD",
        )
        User.objects.create(
            userid="1325110",
            twitterhandle="test2",
            email="test2@test.com",
            password="PASSWORD",
        )
        User.objects.create(
            userid="5230033",
            twitterhandle="test3",
            email="test3@test.com",
            password="PASSWORD",
        )
        User.objects.create(
            userid="1000073",
            twitterhandle="test4",
            email="test4@test.com",
            password="PASSWORD",
        )

        new_object = User.objects.get(twitterhandle="test2")
        new_object.email = "myemail2test@hotmail.com"
        new_object.save()

        new_object = User.objects.get(twitterhandle="test4")
        new_object.email = "email4me@me.com"
        new_object.save()

        response = User.objects.get(twitterhandle="test2")
        response2 = User.objects.get(twitterhandle="test4")

        self.assertEqual(response.email, "myemail2test@hotmail.com")
        self.assertEqual(response2.email, "email4me@me.com")


class TweetTableTests(TestCase):
    """
    These set of tests checks various areas related to the Posts's table.
    """

    def test_tweet_by_user(self):
        User.objects.create(
            userid="5230033",
            twitterhandle="test3",
            email="test3@test.com",
            password="PASSWORD",
        )

    def test_add_tweet(self):
        """
        Adds a new tweet to the database
        """
        test_user = User.objects.create(
            userid="337282",
            twitterhandle="test1",
            email="test1@test.com",
            password="PASSWORD",
        )
        Posts.objects.create(
            postid="1425002",
            tweet="test1",
            userid=test_user,
        )

        num_tweets = Posts.objects.count()

        self.assertEqual(num_tweets, 1)

    def test_add_tweets(self):
        """
        Adds three new tweets to the database
        """
        test_user = User.objects.create(
            userid="337282",
            twitterhandle="test1",
            email="test1@test.com",
            password="PASSWORD",
        )
        Posts.objects.create(
            postid="1425002",
            tweet="test1",
            userid=test_user,
        )
        Posts.objects.create(
            postid="1492332",
            tweet="test2",
            userid=test_user,
        )
        Posts.objects.create(
            postid="1482002",
            tweet="test3",
            userid=test_user,
        )

        num_tweets = Posts.objects.count()

        self.assertEqual(num_tweets, 3)

    def test_get_alltweets(self):
        """
        Gets all tweets from the database
        """
        test_user = User.objects.create(
            userid="337282",
            twitterhandle="test1",
            email="test1@test.com",
            password="PASSWORD",
        )
        Posts.objects.create(
            postid="1482002",
            tweet="test1",
            userid=test_user,
        )
        Posts.objects.create(
            postid="1482007",
            tweet="test2",
            userid=test_user,
        )
        Posts.objects.create(
            postid="1425666",
            tweet="test3",
            userid=test_user,
        )

        response = Posts.objects.all()

        self.assertEqual(len(response), 3)

    def test_get_tweet(self):
        """
        Gets one tweet from the database
        """
        test_user = User.objects.create(
            userid="337282",
            twitterhandle="test1",
            email="test1@test.com",
            password="PASSWORD",
        )
        Posts.objects.create(
            postid="1485402",
            tweet="test1",
            userid=test_user,
        )
        Posts.objects.create(
            postid="1487602",
            tweet="test2",
            userid=test_user,
        )
        Posts.objects.create(
            postid="1481002",
            tweet="test3",
            userid=test_user,
        )

        response = Posts.objects.get(tweet="test2")

        self.assertEqual(response.tweet, "test2")

    def test_get_tweets(self):
        """
        Gets two tweets from the database
        """
        test_user = User.objects.create(
            userid="337282",
            twitterhandle="test1",
            email="test1@test.com",
            password="PASSWORD",
        )
        Posts.objects.create(
            postid="1485402",
            tweet="test1",
            userid=test_user,
        )
        Posts.objects.create(
            postid="1487602",
            tweet="test2",
            userid=test_user,
        )
        Posts.objects.create(
            postid="1481002",
            tweet="test3",
            userid=test_user,
        )

        response1 = Posts.objects.get(tweet="test1")
        response2 = Posts.objects.get(tweet="test3")

        self.assertEqual(response1.tweet, "test1")
        self.assertEqual(response2.tweet, "test3")

    def test_delete_tweet(self):
        """
        Deletes one tweet from the database
        """
        test_user = User.objects.create(
            userid="337282",
            twitterhandle="test1",
            email="test1@test.com",
            password="PASSWORD",
        )
        Posts.objects.create(
            postid="1485402",
            tweet="test1",
            userid=test_user,
        )
        Posts.objects.create(
            postid="1487602",
            tweet="test2",
            userid=test_user,
        )
        Posts.objects.create(
            postid="1481002",
            tweet="test3",
            userid=test_user,
        )
        Posts.objects.create(
            postid="1999999",
            tweet="test4",
            userid=test_user,
        )

        Posts.objects.get(tweet="test1").delete()
        num_posts = Posts.objects.count()

        self.assertEqual(num_posts, 3)

    def test_delete_tweets(self):
        test_user = User.objects.create(
            userid="337282",
            twitterhandle="test1",
            email="test1@test.com",
            password="PASSWORD",
        )
        Posts.objects.create(
            postid="1485402",
            tweet="test1",
            userid=test_user,
        )
        Posts.objects.create(
            postid="1487602",
            tweet="test2",
            userid=test_user,
        )
        Posts.objects.create(
            postid="1481002",
            tweet="test3",
            userid=test_user,
        )
        Posts.objects.create(
            postid="1999999",
            tweet="test4",
            userid=test_user,
        )

        Posts.objects.get(tweet="test1").delete()
        Posts.objects.get(tweet="test4").delete()

        num_posts = Posts.objects.count()

        self.assertEqual(num_posts, 2)

    def test_delete_all(self):
        """
        Deletes all tweets from the database
        """
        test_user = User.objects.create(
            userid="337282",
            twitterhandle="test1",
            email="test1@test.com",
            password="PASSWORD",
        )
        Posts.objects.create(
            postid="1485402",
            tweet="test1",
            userid=test_user,
        )
        Posts.objects.create(
            postid="1487602",
            tweet="test2",
            userid=test_user,
        )
        Posts.objects.create(
            postid="1481002",
            tweet="test3",
            userid=test_user,
        )
        Posts.objects.create(
            postid="1999999",
            tweet="test4",
            userid=test_user,
        )

        Posts.objects.all().delete()
        num_posts = Posts.objects.count()

        self.assertEqual(num_posts, 0)

    def test_update_tweet(self):
        """
        Updates one tweet from the database
        """
        test_user = User.objects.create(
            userid="337282",
            twitterhandle="test1",
            email="test1@test.com",
            password="PASSWORD",
        )
        Posts.objects.create(
            postid="1485402",
            tweet="test1",
            userid=test_user,
        )
        Posts.objects.create(
            postid="1487602",
            tweet="test2",
            userid=test_user,
        )
        Posts.objects.create(
            postid="1481002",
            tweet="test3",
            userid=test_user,
        )
        Posts.objects.create(
            postid="1999999",
            tweet="test4",
            userid=test_user,
        )

        new_post = Posts.objects.get(postid="1481002")
        new_post.tweet = "welcome to the jungle"
        new_post.save()

        response = Posts.objects.get(postid="1481002")

        self.assertEqual(response.tweet, "welcome to the jungle")

    def test_update_tweets(self):
        """
        Updates two tweets from the database
        """
        test_user = User.objects.create(
            userid="337282",
            twitterhandle="test1",
            email="test1@test.com",
            password="PASSWORD",
        )
        Posts.objects.create(
            postid="1485402",
            tweet="test1",
            userid=test_user,
        )
        Posts.objects.create(
            postid="1487602",
            tweet="test2",
            userid=test_user,
        )
        Posts.objects.create(
            postid="1481002",
            tweet="test3",
            userid=test_user,
        )
        Posts.objects.create(
            postid="1999999",
            tweet="test4",
            userid=test_user,
        )

        new_post = Posts.objects.get(postid="1481002")
        new_post.tweet = "welcome to the jungle"
        new_post.save()

        new_post = Posts.objects.get(postid="1485402")
        new_post.tweet = "welcome to the crew"
        new_post.save()

        response1 = Posts.objects.get(postid="1481002")
        response2 = Posts.objects.get(postid="1485402")

        self.assertEqual(response1.tweet, "welcome to the jungle")
        self.assertEqual(response2.tweet, "welcome to the crew")

    """
    def test_update_all(self):
        Posts.objects.create(
        postid="1485402",
        tweet="test1",
        userid=test_user,
        )
        Posts.objects.create(
        postid="1487602",
        tweet="test2",
        userid=test_user,
        )
        Posts.objects.create(
        postid="1481002",
        tweet="test3",
        userid=test_user,
        )
        Posts.objects.create(
        postid="1999999",
        tweet="test4",
        userid=test_user,
        )

        for obj in Posts:
            obj.tweet = "this is my tweet"
            obj.save()

        response1 = User.objects.get(postid="1485402")
        response2 = User.objects.get(postid="1487602")
        response3 = User.objects.get(postid="1481002")
        response4 = User.objects.get(postid="1999999")

        self.assertEqual(response1.status_code, 302)
        self.assertEqual(response1.tweet, "this is my tweet")
        self.assertEqual(response2.status_code, 302)
        self.assertEqual(response2.tweet, "this is my tweet")
        self.assertEqual(response3.status_code, 302)
        self.assertEqual(response3.tweet, "this is my tweet")
        self.assertEqual(response4.status_code, 302)
        self.assertEqual(response4.tweet, "this is my tweet")

    def test_update_all(self):
        User.objects.create(
            userid="337282",
            twitterhandle="test1",
            email="test1@test.com",
            password="PASSWORD",
        )
        User.objects.create(
            userid="1325110",
            twitterhandle="test2",
            email="test2@test.com",
            password="PASSWORD",
        )
        User.objects.create(
            userid="5230033",
            twitterhandle="test3",
            email="test3@test.com",
            password="PASSWORD",
        )
        User.objects.create(
            userid="1000073",
            twitterhandle="test4",
            email="test4@test.com",
            password="PASSWORD",
        )

        for obj in User:
            obj.password = "PA$$WORD"
            obj.save()

        response1 = User.objects.get(twitterhandle="test1")
        response2 = User.objects.get(twitterhandle="test2")
        response3 = User.objects.get(twitterhandle="test3")
        response4 = User.objects.get(twitterhandle="test4")

        self.assertEqual(response1.password, "PA$$WORD")
        self.assertEqual(response2.password, "PA$$WORD")
        self.assertEqual(response3.password, "PA$$WORD")
        self.assertEqual(response4.password, "PA$$WORD")

        
    """
