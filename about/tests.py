from django.test import TestCase
from django.urls import reverse

class TestPage(TestCase):                             def test_home_page_works(self):                       response = self.client.get(reverse("home"))                                                         self.assertEqual(response.status_code, 200)                                                         self.assertTemplateUsed(response, 'homepage.html')                                                  self.assertContains(response, 'Welcome')
