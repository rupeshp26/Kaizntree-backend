import pytest
from dashboard.item.models import Item
from dashboard.category.models import Category
from dashboard.category.serializers import CategorySerializer
from dashboard.item.serializers import ItemSerializer

@pytest.mark.django_db
def test_item_serializer_create(item_data):
    # Test serializer for creating an item
    serializer = ItemSerializer(data=item_data)

    print('serializer--', serializer.is_valid(), item_data, serializer.errors);

    # Check if serializer is valid
    assert serializer.is_valid()

    # Save the item
    item = serializer.save()

    # Check if the item is saved correctly
    assert item.name == 'Test Item'
    assert item.category.name == 'Test Category'
