from decimal import Decimal
from django.test import TestCase
from about import models

class TestModel(TestCase):
    def test_active_manager_works(self):
        models.Product.objects.create(
            name="Italian moccassins",
            price=Decimal("1000.00"))
        models.Product.objects.create(
            name="chinese gown",
            price=Decimal("500"))
        models.Product.objects.create(
            name="Slip on",
            price=Decimal("2.00"),
            active=False)
        self.assertEqual(len(models.Product.objects.active()), 2)