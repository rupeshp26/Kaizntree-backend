from rest_framework.response import Response
from rest_framework import generics, status
from django.contrib.auth.models import User
from dashboard.auth.serializers import UserSerializer
from django.db.models import Q
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate


class UserRegistrationView(generics.CreateAPIView):
    """
    API view for user registration.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        """
        Handle POST request for user registration.
        
        Args:
            request (HttpRequest): The HTTP request object.
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        
        Returns:
            Response: HTTP response indicating the status of the user creation.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            {"message": "User created successfully"},
            status=status.HTTP_201_CREATED
        )

class UserLoginView(generics.CreateAPIView):
    """
    API view for user login.

    This view handles the authentication of users by validating their username and password.
    If the credentials are valid, it returns a response with a token for authentication.

    Methods:
    - post: Handles the POST request for user login.

    Attributes:
    - serializer_class: The serializer class used for user authentication.
    """

    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        """
        Handles the POST request for user login.

        Parameters:
        - request: The HTTP request object.
        - args: Additional positional arguments.
        - kwargs: Additional keyword arguments.

        Returns:
        - Response: The HTTP response object with the authentication token.
        """
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(username=username, password=password)

        if user is None:
            return Response(
                {"error": "Invalid username or password"},
                status=status.HTTP_401_UNAUTHORIZED
            )

        refresh = RefreshToken.for_user(user)
        # return response with set token as cookie
        return Response(
            {
                "message": "Login successful",
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            },
            status=status.HTTP_200_OK
        )
    
