from django.test import TestCase
from tcapi.models import User
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
        Given an email address, return a twitterhandle.
        """
        self.user = User.objects.create(userid="9876543", twitterhandle="test1", email="test1@test.com", password="PASSWORD")
        
    def test_single_users(self):
        """
        Get all users stored in the database.
        """
        twitterhandle = User.objects.get(twitterhandle='test1') 

    def test_get_number_of_users(self):
        """
        Return a single user from the database.
        """
        self.user = User.objects.create(userid="9876543", twitterhandle="test1", email="test1@test.com", password="PASSWORD")
        num_users = User.objects.count()    
        self.assertEqual(num_users, 1)
