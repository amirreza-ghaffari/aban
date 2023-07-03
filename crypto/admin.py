from django.contrib import admin
from .models import CryptoCurrency, CryptoTransaction


class CryptoAdmin(admin.ModelAdmin):
    list_display = ["name", "price"]


class TransactionAdmin(admin.ModelAdmin):
    list_display = ["coin", "user", 'amount', 'is_settlement']
    list_filter = ['coin', 'user', 'is_settlement']


admin.site.register(CryptoCurrency, CryptoAdmin)
admin.site.register(CryptoTransaction, TransactionAdmin)
