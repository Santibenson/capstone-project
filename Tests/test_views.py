
from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from Restaurant.models import Menu
from API.serializers import MenuSerializer



class MenuViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        Menu.objects.create(title="Milkshake", price="3000", inventory="10")
        Menu.objects.create(title="Pineapple Juice", price="1500", inventory="15")
        Menu.objects.create(title="Pina Colada", price="4000", inventory="5")
        Menu.objects.create(title="Sex on the beach", price="3500", inventory="8")

    def test_getall(self):
        response = self.client.get(reverse('menu'))
        menu_ = Menu.objects.all()
        serializer = MenuSerializer(menu_, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.data, status.HTTP_200_OK)
