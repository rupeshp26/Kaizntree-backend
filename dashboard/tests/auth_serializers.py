import pytest
from django.contrib.auth.models import User
from dashboard.auth.serializers import UserSerializer

@pytest.mark.django_db
def test_user_serializer_create(user_data):
    # Test serializer for creating a user
    serializer = UserSerializer(data=user_data)

    # Check if serializer is valid
    assert serializer.is_valid()

    # Save the user
    user = serializer.save()

    # Check if the user is saved correctly
    assert user.username == 'testuser'
    assert user.check_password('password123')

@pytest.mark.django_db
def test_user_serializer_password_not_returned(user_data):
    # Test that password field is not returned in serializer data
    serializer = UserSerializer(data=user_data)

    # Check if serializer is valid
    assert serializer.is_valid()

    # Check that 'password' is not in serializer data
    assert 'password' not in serializer.data