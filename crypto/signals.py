from django.db.models.signals import post_save
from .models import CryptoTransaction
from django.db.models import F, Sum
from django.db import transaction
from .tools import buy_from_exchange


def withdraw_foreign_exchanger(sender, instance, created, **kwargs):
    if created:
        if instance.amount * instance.coin.price < 10:
            crypto_tr_qs = CryptoTransaction.objects.select_for_update().filter(is_settlement=False, coin=instance.coin)
            with transaction.atomic():
                aggregated = crypto_tr_qs.annotate(value=F('amount') * F('coin__price')).aggregate(total=Sum('value'))
                value = aggregated.get('total', 0)
                if value >= 10:
                    for obj in crypto_tr_qs:
                        obj.is_settlement = True
                        obj.save()
                    buy_from_exchange(crypto_name=instance.coin.name, amount=value/instance.coin.price)


post_save.connect(withdraw_foreign_exchanger, sender=CryptoTransaction)
