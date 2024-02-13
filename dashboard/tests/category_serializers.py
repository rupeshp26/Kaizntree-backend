import pytest
from dashboard.category.models import Category
from dashboard.category.serializers import CategorySerializer

@pytest.mark.django_db
def test_category_serializer():
    # Create a category instance
    category = Category.objects.create(name='Test Category')

    # Initialize serializer with the category instance
    serializer = CategorySerializer(instance=category)

    # Validate serializer data
    assert serializer.data['id'] == category.id
    assert serializer.data['name'] == category.name

@pytest.mark.django_db
def test_category_serializer_create():
    # Test serializer for creating a category
    data = {'name': 'New Test Category'}
    serializer = CategorySerializer(data=data)

    # Check if serializer is valid
    assert serializer.is_valid()

    # Save the category
    category = serializer.save()

    # Check if the category is saved correctly
    assert category.name == 'New Test Category'
