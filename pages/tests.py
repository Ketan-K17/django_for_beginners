
from django.test import SimpleTestCase
from django.urls import reverse

class HomepageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "home.html")

    def test_template_content(self):
        response = self.client.get(reverse("home"))
        self.assertContains(response, "<h1>Company Homepage</h1>")

class AboutpageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/about/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse("about"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        response = self.client.get(reverse("about"))
        self.assertTemplateUsed(response, "about.html")

    def test_template_content(self):
        response = self.client.get(reverse("about"))
        self.assertContains(response, "<h1>Company About Page</h1>")

# NOTE: What's the reverse() method? 
# reverse() is a Django function that returns the URL for a given view name. It is used to generate URLs for views in your templates. Basically the equivalent of the 'url' tag in python. Use this to further not have to hardcode urls in your view / test files..

# reverse("about") → "/about/"
# {% url "about" %} → calls reverse("about") internally → "/about/"

# NOTE: assertContains() and assertTemplateUsed() are Django test assertions that check if a response contains a specific string or template is used. Use this to be absolutely sure the right template is being accessed.
