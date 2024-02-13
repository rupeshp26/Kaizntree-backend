from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from django.db import IntegrityError
from dashboard.category.models import Category
from dashboard.category.serializers import CategorySerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

class CategoryCreateView(generics.CreateAPIView):
    """
    API view for creating a new category.

    This view requires JWT authentication and the user must be authenticated.
    It handles the HTTP POST request and creates a new category using the provided data.

    If a category with the same key already exists, it returns a 400 Bad Request response.

    Attributes:
        authentication_classes (list): List of authentication classes used for this view.
        permission_classes (list): List of permission classes used for this view.
        queryset (QuerySet): Queryset of all Category objects.
        serializer_class (Serializer): Serializer class used for serializing and deserializing Category objects.

    Methods:
        post(request, *args, **kwargs): Handles the HTTP POST request and creates a new category.

    """
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def post(self, request, *args, **kwargs):
        """
        Handles the HTTP POST request and creates a new category.

        Args:
            request (HttpRequest): The HTTP request object.
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            Response: The HTTP response object.

        Raises:
            IntegrityError: If a category with the same key already exists.

        """
        try:
            print(request.data)
            return super().post(request, *args, **kwargs)
        except IntegrityError:
            return Response({"error": "Category with the same key already exists"}, status=status.HTTP_400_BAD_REQUEST)

