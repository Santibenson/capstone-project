from django.test import TestCase
from Restaurant.models import Menu

class MenuTest(TestCase):
    def test_create_item(self):
        item = Menu.objects.create(title="Sandwich", price="1500.00", inventory="80")
        self.assertEqual(item.__str__(), "Sandwich : 1500.00")