from rest_framework import serializers
from dashboard.category.models import Category

class CategorySerializer(serializers.ModelSerializer):
    """
    Serializer for the Category model.

    Serializes the Category model fields 'id' and 'name'.
    """
    class Meta:
        model = Category
        fields = ['id', 'name']

