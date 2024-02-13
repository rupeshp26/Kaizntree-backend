import pytest
from rest_framework.test import APIClient

@pytest.fixture
def user_data():
    return {
        'username': 'testuser',
        'password': 'password123'
    }


@pytest.fixture
def category_data():
    return {
        'name': 'Test Category'
    }

@pytest.mark.django_db
@pytest.fixture
def item_data(category_data):
    return {
        'name': 'Test Item',
        'sku': 'Test SKU Name',
        'category': category_data,
        'available_stock':10, 
        'in_stock':7,
        'stock_status': True
    }

@pytest.fixture
def api_client():
    return APIClient()