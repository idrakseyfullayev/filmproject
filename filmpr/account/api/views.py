from rest_framework.generics import (
    ListAPIView, CreateAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView)
from django.contrib.auth.models import User
from account.models import Account
from account.api.serializers import (
UserListSerializer, UserCreateSerializer, UserUpdtaeSerializer,
AccountListSerializer, AccountCreateSerializer, AccountUpdateSerializer,
)

class UserListAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer

class UserCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer

class UserUpdateAPIView(RetrieveUpdateAPIView):
    queryset = User.objects.all()
    lookup_field = "id"
    serializer_class = UserUpdtaeSerializer

class UserDestroyAPIView(RetrieveDestroyAPIView):
    queryset = User.objects.all()
    lookup_field = "id"
    serializer_class = UserListSerializer    


class AccountListAPIView(ListAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountListSerializer

class AccountCreateAPIView(CreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountCreateSerializer

class AccountUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Account.objects.all()
    lookup_field = "id"
    serializer_class = AccountUpdateSerializer

class AccountDestroyAPIView(RetrieveDestroyAPIView):
    queryset = Account.objects.all()
    lookup_field = "id"
    serializer_class = AccountListSerializer     

    
       


