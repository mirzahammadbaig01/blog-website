# user/urls.py
from django.urls import path
from .views import UserRegistrationView
from rest_framework.authtoken.views import obtain_auth_token
from .views import UserProfileView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', obtain_auth_token, name='login'),
    path('profile/', UserProfileView.as_view(), name='profile'),
]
