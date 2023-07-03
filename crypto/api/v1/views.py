from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import viewsets, status
from ...models import CryptoCurrency, Wallet, CryptoTransaction
from .serializers import TransactionSerializer
from django.shortcuts import get_object_or_404
from ...tools import buy_from_exchange
from django.db import transaction
from users.models import CustomUser, TomanWallet


class TransactionViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving Transactions.
    """
    def list(self, request):
        queryset = CryptoTransaction.objects.all()
        serializer = TransactionSerializer(queryset, many=True)
        return Response(serializer.data)


@api_view(['POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def do_transaction(request):

    data = request.data
    user = request.user
    coin_name = data.get('coin_name')
    amount = data.get('amount')
    if coin_name and amount:
        coin = get_object_or_404(CryptoCurrency, name=coin_name)
        value = coin.price * amount
        try:
            with transaction.atomic():

                user_wallet = TomanWallet.objects.select_for_update().get(user=user)
                user_wallet.balance -= value
                user_wallet.save()

                if value >= 10:
                    tr = CryptoTransaction(user=user, coin=coin, amount=amount, is_settlement=True)
                    tr.save()
                    buy_from_exchange(crypto_name=coin_name, amount=amount)
                else:
                    # This Section will Call a signal in crypto/signals.py
                    tr = CryptoTransaction(user=user, coin=coin, amount=amount, is_settlement=False)
                    tr.save()

                return Response({"message": "Transaction was successful"}, status=status.HTTP_200_OK)
        except:
            return Response({"message": "something went wrong"}, status=status.HTTP_400_BAD_REQUEST)

    return Response({"message": "amount or coin is missing"}, status=status.HTTP_400_BAD_REQUEST)






