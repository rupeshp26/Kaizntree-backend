import pytest
from django.urls import reverse
from rest_framework import status
from dashboard.item.models import Item
from dashboard.category.models import Category

@pytest.mark.django_db
def test_item_list_view(api_client):
    # Create some test data
    category = Category.objects.create(name='Test Category')
    # Assuming available_stock is a required field
    Item.objects.create(
        name='Test Item 1', 
        sku='SKU1', 
        category=category, 
        available_stock=10, 
        in_stock=7,
        stock_status=True
    )

    # Make a GET request to the ItemListView
    response = api_client.get(reverse('item-list'))

    # Check that the response status code is 200 OK
    assert response.status_code == status.HTTP_200_OK

    # Check that the response contains the expected data
    assert 'total_items' in response.data
    assert 'total_categories' in response.data
    assert 'items' in response.data
    assert len(response.data['items']) == 1  # Assuming only 1 item is created


@pytest.mark.django_db
def test_item_create_view(api_client, category_data):
    # Create a test category
    category = Category.objects.create(name='Test Category')

    # Define data for creating a new item
    item_data = {
        'name': 'Test Item',
        'sku': 'SKU123',
        'category': category_data,
        'available_stock':10, 
        'in_stock':7,
        'stock_status': True
    }

    # Make a POST request to the ItemCreateView
    response = api_client.post(
        reverse('item-create'),
        data=item_data, 
        format='json'
    )
    print('response--', response.content);

    # Check that the response status code is 201 Created
    assert response.status_code == status.HTTP_201_CREATED

    # Check that the item was created in the database
    assert Item.objects.filter(name='Test Item').exists()
