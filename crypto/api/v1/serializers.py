from rest_framework import serializers
from ...models import (
    CryptoTransaction,
    CryptoCurrency
)
from users.models import CustomUser
from django.shortcuts import get_object_or_404
from ...tools import buy_from_exchange


class CryptoCurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = CryptoCurrency
        fields = ['name']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('full_name', 'id', )


class TransactionSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    coin_name = serializers.CharField(source='coin.name')

    class Meta:
        model = CryptoTransaction
        fields = ['user', 'amount', 'coin_name']
        read_only_fields = ['user']
        depth = 1






