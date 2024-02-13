from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from dashboard.item.views import ItemListView, ItemCreateView, HomeView
from dashboard.auth.views import UserRegistrationView, UserLoginView
from dashboard.category.views import CategoryCreateView


urlpatterns = [
    # Auth Routes
    path('', HomeView.as_view(), name='home'),
    path('', UserRegistrationView.as_view(), name='home'),
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    # Dashboard Item Routes
    path('items/', ItemListView.as_view(), name='item-list'),
    path('items/create/', ItemCreateView.as_view(), name='item-create'),
    # Category Routes
    path('categories/create/', CategoryCreateView.as_view(), name='category-create'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
