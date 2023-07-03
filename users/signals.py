from django.db.models.signals import post_save
from users.models import TomanWallet, CustomUser


def create_wallet(sender, instance, created, **kwargs):
    if created:
        TomanWallet(user=instance, balance=0).save()


post_save.connect(create_wallet, sender=CustomUser)
