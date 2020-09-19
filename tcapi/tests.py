from django.test import SimpleTestCase


class SimpleTests(SimpleTestCase):
    """
    This class tests that a connection is made to our API.
    """
    def test_api_get_pass(self):
        """
        GET request to our api returning a 200 status code.
        """
        response = self.client.get('/index.html')
        self.assertEqual(response.status_code, 200)

    def test_api_get_fail(self):
        """
        GET request to our api returning a 200 status code.
        """
        response = self.client.get('/missing.html')
        self.assertEqual(response.status_code, 200)

