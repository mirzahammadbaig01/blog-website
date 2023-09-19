from rest_framework import generics
from .serializers import UserSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from .serializers import UserProfileSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response



class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserSerializer

class UserLoginView(ObtainAuthToken):
    pass

class UserProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserProfileSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user
