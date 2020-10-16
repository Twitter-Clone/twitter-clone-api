from django.test import TestCase

from django.test import TestCase
from tcapi.models import User, Posts
from django.test.client import Client


class StatusTests(TestCase):
    """
    This class tests that a connection is made to our API.
    """
    def setUp(self):
       self.client = Client()

    def test_api_get_pass(self):
        """
        GET request to our api returning a 200 status code.
        """
        response = self.client.get('/api/tcapi')
        self.assertEqual(response.status_code, 200)

class UserTableTests(TestCase):
    """
    This set of tests checks various areas related to the User's table.
    """
    def test_add_user(self):
        """
        Adds a new user
        """
        self.user = User.objects.create(userid="9876543", twitterhandle="test1", email="test1@test.com", password="PASSWORD")
        num_users = User.objects.count()
        self.assertEqual(num_users, 1)
        
    def test_add_users(self):
        """
        Adds multiple users
        """
        self.user1 = User.objects.create(userid="1357924", twitterhandle="test1", email="test1@test.com", password="PASSWORD")
        self.user2 = User.objects.create(userid="9876543", twitterhandle="test2", email="test2@test.com", password="PASSWORD")
        self.user3 = User.objects.create(userid="1234567", twitterhandle="test3", email="test3@test.com", password="PASSWORD")
         
        num_users = User.objects.count()    
        self.assertEqual(num_users, 3)
        
    def test_get_users(self):
        """
        Get all users stored in the database.
        """
        self.user = User.objects.create(userid="9876543", twitterhandle="test1", email="test1@test.com", password="PASSWORD")
        self.user2 = User.objects.create(userid="9879874", twitterhandle="test2", email="test1@test.com", password="PASSWORD")
        self.user3 = User.objects.create(userid="1746213", twitterhandle="test3", email="test1@test.com", password="PASSWORD")
        twitterhandle = User.objects.get()
        if twitterhandle is not NULL:
            self.assertEqual(1,1)
        else:
            self.assertEqual(0,1)
        
    def test_get_user(self):
        """
        Given an email address, return a twitterhandle.
        """
        self.user = User.objects.create(userid="9876543", twitterhandle="test1", email="test1@test.com", password="PASSWORD")
        twitterhandle = User.objects.get(twitterhandle="test1")
        self.assertEqual(twitterh, User.objects.get(email="test1@test.com"))
    
    def test_delete_users(self):
        """
        Creates and deletes all users from the database
        """
        self.user = User.objects.create(userid="1322253", twitterhandle="test1", email="test1@test.com", password="PASSWORD")
        self.user = User.objects.create(userid="1325110", twitterhandle="test2", email="test2@test.com", password="PASSWORD")
        self.user = User.objects.create(userid="5230033", twitterhandle="test3", email="test3@test.com", password="PASSWORD")
        self.user = User.objects.create(userid="1000073", twitterhandle="test4", email="test4@test.com", password="PASSWORD")
        
        User.objects.get.all().delete()
        num_users = User.objects.count()
        self.assertEqual(num_users, 0)
        
    def test_delete_user(self):
        """
        Creates and deletes one user from the database
        """
        self.user = User.objects.create(userid="1322253", twitterhandle="test1", email="test1@test.com", password="PASSWORD")
        self.user = User.objects.create(userid="1325110", twitterhandle="test2", email="test2@test.com", password="PASSWORD")
        self.user = User.objects.create(userid="5230033", twitterhandle="test3", email="test3@test.com", password="PASSWORD")
        self.user = User.objects.create(userid="1000073", twitterhandle="test4", email="test4@test.com", password="PASSWORD")
        
        User.objects.get(twitterhandle="test1").delete()
        num_users = User.objects.count()
        self.assertEqual(num_users, 3)
        
class TweetTableTests(TestCase):
    """
    This set of tests checks various areas related to the User's table.
    """
    def test_add_tweet(self):
        """
        Creates a new tweet
        """
        self.tweet = Posts.objects.create(postid="1425002", tweet="test1", userid_id="1322253")
        num_users = User.objects.count()
        self.assertEqual(num_users, 1)
        
