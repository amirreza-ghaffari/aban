from django.db import models
from users.models import CustomUser
from lib.base_model import AbstractModel


class CryptoCurrency(models.Model):
    name = models.CharField(max_length=256)
    price = models.FloatField()

    def __str__(self):
        return self.name


class Wallet(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.PROTECT)
    coin = models.ForeignKey(CryptoCurrency, on_delete=models.PROTECT)
    amount = models.FloatField()

    def __str__(self):
        return str(self.coin) + '-' + str(self.amount)


class CryptoTransaction(AbstractModel):
    user = models.ForeignKey(CustomUser, on_delete=models.PROTECT)
    coin = models.ForeignKey(CryptoCurrency, on_delete=models.PROTECT)
    amount = models.FloatField()

    # show that this object has been settled with foreign exchanger or not
    is_settlement = models.BooleanField(default=False, db_index=True)

    def __str__(self):
        return self.coin.name + '-' + str(self.amount)

    @property
    def transaction_value(self):
        return self.coin.price * self.amount




    



