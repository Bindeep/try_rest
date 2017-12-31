from rest_framework import viewsets
from .serializers import UserSerializer
from django.contrib.auth.models import User
from customer.models import Customer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer