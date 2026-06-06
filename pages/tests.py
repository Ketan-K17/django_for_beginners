from django.test import TestCase, SimpleTestCase

class HomepageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        
class AboutpageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/about/")
        self.assertEqual(response.status_code, 200)


# NOTE: There are 4 types of unit tests in Django (these are extensions of the base unittest class in python)
# 1. SimpleTestCase: for testing views that don't require a database (e.g. views that just return a static response)
# 2. TestCase: for testing views that require a database (e.g. views that query the database)
# 3. TransactionTestCase: for testing views that require a database (e.g. views that query the database) and need to be rolled back after the test is complete (e.g. to avoid side effects on the database)
# 4. LiveServerTestCase: for testing views that require a live server (e.g. views that test the server's response)