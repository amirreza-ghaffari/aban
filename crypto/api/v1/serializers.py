from rest_framework import serializers
from ...models import CryptoTransaction, CryptoCurrency


class CryptoCurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = CryptoCurrency
        fields = ['name']


class TransactionSerializer(serializers.ModelSerializer):
    coin = CryptoCurrencySerializer(many=False, read_only=True)
    class Meta:
        model = CryptoTransaction
        fields = ['user', 'coin', 'amount']







