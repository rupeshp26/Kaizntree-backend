from django.db import models
from dashboard.category.models import Category

class Item(models.Model):
    """
    Represents an item in the inventory.

    Attributes:
        sku (str): The SKU (Stock Keeping Unit) of the item.
        name (str): The name of the item.
        category (Category): The category to which the item belongs.
        tags (str): Any additional tags associated with the item.
        available_stock (int): The quantity of the item available for sale.
        in_stock (int): The total quantity of the item in stock.
        stock_status (bool): The status of the item's stock (True if in stock, False otherwise).
    """

    sku = models.CharField(max_length=100)
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.TextField(blank=True)
    available_stock = models.IntegerField()
    in_stock = models.IntegerField()
    stock_status = models.BooleanField()

    def __str__(self):
        return self.name
    
