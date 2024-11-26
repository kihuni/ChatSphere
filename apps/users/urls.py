# apps/users/urls.py
from django.urls import path
from .views import UserRegistrationAPIView, UserProfileAPIView


urlpatterns = [
    path('register/', UserRegistrationAPIView.as_view(), name='register'),
    path('profile/', UserProfileAPIView.as_view(), name='profile'),
]