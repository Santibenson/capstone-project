
from django.test import TestCase, RequestFactory
from rest_framework import status
from Restaurant.models import Menu
from API.serializers import MenuSerializer
from API.views import MenuItemView


class MenuViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

        self.milkshake = Menu.objects.create(title="Milkshake", price=3000, inventory=10)
        self.pineapple = Menu.objects.create(title="Pineapple Juice", price=3000, inventory=10)

    def test_getall(self):
        menu_ = Menu.objects.all()
        serializer = MenuSerializer(menu_, many=True)
        request = self.factory.get('restaurant/api/menu')
        response = MenuItemView.as_view()(request)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.data, status.HTTP_200_OK)
