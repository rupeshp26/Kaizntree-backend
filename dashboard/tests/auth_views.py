import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIRequestFactory
from dashboard.auth.views import UserRegistrationView, UserLoginView

@pytest.mark.django_db
def test_user_registration_view(user_data):
    # Test user registration view
    factory = APIRequestFactory()
    request = factory.post('/register/', user_data)
    view = UserRegistrationView.as_view()

    response = view(request)

    assert response.status_code == 201
    assert User.objects.filter(username='testuser').exists()

@pytest.mark.django_db
def test_user_login_view(user_data):
    # Create a test user
    User.objects.create_user(username='testuser', password='password123')

    # Test user login view
    factory = APIRequestFactory()
    request = factory.post('/login/', {'username': 'testuser', 'password': 'password123'})
    view = UserLoginView.as_view()

    response = view(request)

    assert response.status_code == 200
    assert 'refresh' in response.data
    assert 'access' in response.data
