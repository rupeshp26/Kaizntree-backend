from rest_framework import serializers
from dashboard.item.models import Item
from dashboard.category.models import Category
from dashboard.category.serializers import CategorySerializer

class ItemSerializer(serializers.ModelSerializer):
    """
    Serializer class for Item model.
    """

    category = CategorySerializer()  # Use CategorySerializer for read/write

    class Meta:
        model = Item
        fields = '__all__'

    def create(self, validated_data):
        """
        Create a new Item instance.

        Args:
            validated_data (dict): Validated data for creating the Item instance.

        Returns:
            Item: The created Item instance.
        """
        category_data = validated_data.pop('category')
        category_instance, created = Category.objects.get_or_create(**category_data)     # Get or create category
        item_instance = Item.objects.create(category=category_instance, **validated_data)
        return item_instance

