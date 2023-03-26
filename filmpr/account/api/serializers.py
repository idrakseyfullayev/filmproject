from rest_framework import serializers
from django.contrib.auth.models import User
from account.models import Account

class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ("password",)
        

class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class UserUpdtaeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class AccountListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = "__all__"

class AccountCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = "__all__"

class AccountUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = "__all__"

        