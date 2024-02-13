from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from dashboard.category.models import Category

class CategoryCreateViewTestCase(APITestCase):
    def test_create_category(self):
        url = reverse('category-create')
        data = {'name': 'Test Category'}

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Category.objects.count(), 1)
        self.assertEqual(Category.objects.get().name, 'Test Category')
