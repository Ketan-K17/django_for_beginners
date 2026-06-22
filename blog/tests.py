from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from .models import Blogpost

class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="testuser", email="test@email.com", password="secret"
        )

        cls.blogpost = Blogpost.objects.create(
            title="A good title",
            body="Nice body content",
            author=cls.user,
        )

    def test_post_model(self):
        self.assertEqual(self.blogpost.title, "A good title")
        self.assertEqual(self.blogpost.body, "Nice body content")
        self.assertEqual(self.blogpost.author.username, "testuser")
        self.assertEqual(str(self.blogpost), "A good title - by testuser")
        self.assertEqual(self.blogpost.get_absolute_url(), "/blog/blogpost/1/")

    def test_blogpost_list_url_exists(self):
        response = self.client.get("/blog/")
        self.assertEqual(response.status_code, 200)

    def test_blogpost_detail_url_exists(self):
        response = self.client.get(f"/blog/blogpost/{self.blogpost.pk}/")
        self.assertEqual(response.status_code, 200)

    def test_blogpost_list_url_by_name(self):
        response = self.client.get(reverse("blog:home"))
        self.assertEqual(response.status_code, 200)

    def test_blogpost_detail_url_by_name(self):
        response = self.client.get(reverse("blog:blogpost_detail", kwargs={"pk": self.blogpost.pk}))
        self.assertEqual(response.status_code, 200)

    def test_blogpost_list_template(self):
        response = self.client.get(reverse("blog:home"))
        self.assertTemplateUsed(response, "blog/blog.html")

    def test_blogpost_detail_template(self):
        response = self.client.get(reverse("blog:blogpost_detail", kwargs={"pk": self.blogpost.pk}))
        self.assertTemplateUsed(response, "blog/blogpost_detail.html")

    def test_blogpost_list_template_content(self):
        response = self.client.get(reverse("blog:home"))
        self.assertContains(response, "A good title")
        self.assertContains(response, "Nice body content")

    def test_blogpost_detail_template_content(self):
        response = self.client.get(reverse("blog:blogpost_detail", kwargs={"pk": self.blogpost.pk}))
        self.assertContains(response, "A good title")
        self.assertContains(response, "Nice body content")
        self.assertContains(response, "testuser")