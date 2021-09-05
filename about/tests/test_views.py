from django.test import TestCase
from django.urls import reverse
from about import forms


class TestPage(TestCase):
    def test_home_page_works(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'homepage.html')
        self.assertContains(response, 'Traderii')


    def test_about_page_works(self):
        response = self.client.get(reverse("about_us"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about_us.html')
        self.assertContains(response, 'company')


    def test_contact_us_page_works(self):
        response = self.client.get(reverse("contact_us"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact_us.html')
        self.assertContains(response, 'fill')
        self.assertIsInstance(response.context["form"], forms.ContactForm)
