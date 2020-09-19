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

    def test_api_post_pass(self):
        """
        POST request to our api returning a 200 status code.
        """
        response = self.client.post('/index.html')
        self.assertEqual(response.status_code, 200)

    def test_api_post_fail(self):
        """
        GET request to our api returning a 200 status code.
        """
        response = self.client.post('/missing.html')
        self.assertEqual(response.status_code, 200)

    def test_api_put_pass(self):
        """
        PUT request to our api returning a 200 status code.
        """
        response = self.client.put('/index.html')
        self.assertEqual(response.status_code, 200)

    def test_api_put_fail(self):
        """
        PUT request to our api returning a 200 status code.
        """
        response = self.client.put('/missing.html')
        self.assertEqual(response.status_code, 200)

    def test_api_delete_pass(self):
        """
        DELETE request to our api returning a 200 status code.
        """
        response = self.client.delete('/index.html')
        self.assertEqual(response.status_code, 200)

    def test_api_delete_fail(self):
        """
        DELETE request to our api returning a 200 status code.
        """
        response = self.client.delete('/missing.html')
        self.assertEqual(response.status_code, 200)
