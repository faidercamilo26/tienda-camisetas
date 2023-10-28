from rest_framework.views import APIView
from rest_framework import generics
from core.models.user import User
from core.serializers.userSerializer import UserSerializer


class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
