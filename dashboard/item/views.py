from rest_framework.response import Response
from rest_framework import generics
from dashboard.item.models import Item
from dashboard.category.models import Category
from dashboard.item.serializers import ItemSerializer
from django.views.decorators.cache import cache_page
from django.db.models import Q
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.pagination import PageNumberPagination

class HomeView(generics.ListAPIView):
    def list(self, request, *args, **kwargs):
        # Your custom logic to generate the response
        data = {'message': 'Hello, this is a custom response from HomeView!'}
        
        # Return a Response instance with your data
        return Response(data)

class ItemListView(generics.ListAPIView):
    """
    API view for listing items with various filtering options.

    Supported query parameters:
    - search_term: Search term to filter items by SKU, name, category, tags, stock status, available stock, and in stock.
    - sku: Filter items by SKU.
    - name: Filter items by name.
    - category: Filter items by category (supports multiple values).
    - tags: Filter items by tags (supports multiple values).
    - stock_status: Filter items by stock status.
    - available_stock_min: Filter items by minimum available stock.
    - available_stock_max: Filter items by maximum available stock.
    - in_stock_min: Filter items by minimum in stock.
    - in_stock_max: Filter items by maximum in stock.

    Returns a JSON response with the following data:
    - total_items: Total count of items.
    - total_categories: Total count of categories.
    - items: Serialized data of the filtered items.
    """
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def dispatch(self, *args, **kwargs):
        return cache_page(60 * 15)(super().dispatch)(*args, **kwargs)

    # Rest of the code...
class ItemListView(generics.ListAPIView):
    """
    API view for listing items with various filtering options.

    Supported query parameters:
    - search_term: Search term to filter items by SKU, name, category, tags, stock status, available stock, and in stock.
    - sku: Filter items by SKU.
    - name: Filter items by name.
    - category: Filter items by category (supports multiple values).
    - tags: Filter items by tags (supports multiple values).
    - stock_status: Filter items by stock status.
    - available_stock_min: Filter items by minimum available stock.
    - available_stock_max: Filter items by maximum available stock.
    - in_stock_min: Filter items by minimum in stock.
    - in_stock_max: Filter items by maximum in stock.

    Returns a JSON response with the following data:
    - total_items: Total count of items.
    - total_categories: Total count of categories.
    - items: Serialized data of the filtered items.
    """
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def dispatch(self, *args, **kwargs):
        return cache_page(60 * 15)(super().dispatch)(*args, **kwargs)
    
class ItemListView(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    pagination_class = PageNumberPagination
    page_size = 5

    def dispatch(self, *args, **kwargs):
        return cache_page(60 * 15)(super().dispatch)(*args, **kwargs)

    def get_queryset(self):
        filters = {}

        # Get filter options from query parameters
        search_term = self.request.query_params.get('search_term')
        sku = self.request.query_params.get('sku')
        name = self.request.query_params.get('name')
        categories = self.request.query_params.getlist('category')  # Allow multiple values
        tags = self.request.query_params.getlist('tags')  # Allow multiple values
        stock_status = self.request.query_params.get('stock_status')
        available_stock_min = self.request.query_params.get('available_stock_min')
        available_stock_max = self.request.query_params.get('available_stock_max')
        in_stock_min = self.request.query_params.get('in_stock_min')  # Additional filter for 'in_stock'
        in_stock_max = self.request.query_params.get('in_stock_max')  # Additional filter for 'in_stock'

        # Validate and add filters to the dictionary
        if search_term:
            filters['search'] = (
                Q(sku__iexact=search_term) |
                Q(name__iexact=search_term) |
                Q(category_name_iexact=search_term) |  # Assuming Category has a 'name' field
                Q(tags__iexact=search_term) |
                Q(stock_status__iexact=search_term) |
                Q(available_stock__iexact=search_term) |
                Q(in_stock__iexact=search_term)  # Additional condition for 'in_stock'
            )

        if sku:
            filters['sku'] = Q(sku__iexact=sku)

        if name:
            filters['name'] = Q(name__iexact=name)

        if categories:
            # Allow filtering based on multiple values for the 'category' column
            category_filter = Q()
            for category in categories:
                category_filter |= Q(category_name_iexact=category)
            filters['categories'] = category_filter

        if tags:
            # Allow filtering based on multiple values for the 'tags' column
            tags_filter = Q()
            for tag in tags:
                tags_filter |= Q(tags__iexact=tag)
            filters['tags'] = tags_filter

        if stock_status:
            filters['stock_status'] = Q(stock_status__iexact=stock_status)

        if available_stock_min is not None and available_stock_max is not None:
            # Allow filtering based on a range for 'available_stock'
            filters['available_stock_range'] = Q(available_stock__range=(available_stock_min, available_stock_max))

        if in_stock_min is not None and in_stock_max is not None:
            # Allow filtering based on a range for 'in_stock'
            filters['in_stock_range'] = Q(in_stock__range=(in_stock_min, in_stock_max))

        queryset = Item.objects.all()

        # Apply filters to the queryset
        for key, value in filters.items():
            queryset = queryset.filter(value)

        return queryset
    
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = ItemSerializer(queryset, many=True)
        page = self.paginate_queryset(queryset)

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)

        # Get the total count of items
        total_items = Item.objects.count()

        # Get the total count of categories
        total_categories = Category.objects.count()

        response_data = {
            'total_items': total_items,
            'total_categories': total_categories,
            'items': serializer.data,
        }

        return Response(response_data)

    # Rest of the code...
# class ItemListView(generics.ListAPIView):
#     authentication_classes = [JWTAuthentication]
#     permission_classes = [IsAuthenticated]
#     queryset = Item.objects.all()
#     serializer_class = ItemSerializer

#     def dispatch(self, *args, **kwargs):
#         return cache_page(60 * 15)(super().dispatch)(*args, **kwargs)

    
#     def get_queryset(self):
#         filters = {}

#         # Get filter options from query parameters
#         search_term = self.request.query_params.get('search_term')
#         sku = self.request.query_params.get('sku')
#         name = self.request.query_params.get('name')
#         categories = self.request.query_params.getlist('category')  # Allow multiple values
#         tags = self.request.query_params.getlist('tags')  # Allow multiple values
#         stock_status = self.request.query_params.get('stock_status')
#         available_stock_min = self.request.query_params.get('available_stock_min')
#         available_stock_max = self.request.query_params.get('available_stock_max')
#         in_stock_min = self.request.query_params.get('in_stock_min')  # Additional filter for 'in_stock'
#         in_stock_max = self.request.query_params.get('in_stock_max')  # Additional filter for 'in_stock'

#         # Validate and add filters to the dictionary
#         if search_term:
#             filters['search'] = (
#                 Q(sku__iexact=search_term) |
#                 Q(name__iexact=search_term) |
#                 Q(category__name__iexact=search_term) |  # Assuming Category has a 'name' field
#                 Q(tags__iexact=search_term) |
#                 Q(stock_status__iexact=search_term) |
#                 Q(available_stock__iexact=search_term) |
#                 Q(in_stock__iexact=search_term)  # Additional condition for 'in_stock'
#             )

#         if sku:
#             filters['sku'] = Q(sku__iexact=sku)

#         if name:
#             filters['name'] = Q(name__iexact=name)

#         if categories:
#             # Allow filtering based on multiple values for the 'category' column
#             category_filter = Q()
#             for category in categories:
#                 category_filter |= Q(category__name__iexact=category)
#             filters['categories'] = category_filter

#         if tags:
#             # Allow filtering based on multiple values for the 'tags' column
#             tags_filter = Q()
#             for tag in tags:
#                 tags_filter |= Q(tags__iexact=tag)
#             filters['tags'] = tags_filter

#         if stock_status:
#             filters['stock_status'] = Q(stock_status__iexact=stock_status)

#         if available_stock_min is not None and available_stock_max is not None:
#             # Allow filtering based on a range for 'available_stock'
#             filters['available_stock_range'] = Q(available_stock__range=(available_stock_min, available_stock_max))

#         if in_stock_min is not None and in_stock_max is not None:
#             # Allow filtering based on a range for 'in_stock'
#             filters['in_stock_range'] = Q(in_stock__range=(in_stock_min, in_stock_max))

#         queryset = Item.objects.all()

#         # Apply filters to the queryset
#         for key, value in filters.items():
#             queryset = queryset.filter(value)

#         return queryset
    
    
    
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = ItemSerializer(queryset, many=True)

        # Get the total count of items
        total_items = Item.objects.count()

        # Get the total count of categories
        total_categories = Category.objects.count()

        response_data = {
            'total_items': total_items,
            'total_categories': total_categories,
            'items': serializer.data,
        }

        return Response(response_data)
    
class ItemCreateView(generics.CreateAPIView):
    """
    View for creating a new item.

    This view requires JWT authentication and the user must be authenticated.
    It uses the ItemSerializer to serialize and validate the input data.
    """

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def perform_create(self, serializer):
        serializer.save()
