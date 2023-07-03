from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views


app_name = "api-v1"


urlpatterns = [
    path('do_transaction/', views.do_transaction),
]

router = DefaultRouter()
router.register(r'transactions', views.TransactionViewSet, basename='transactions')
urlpatterns = urlpatterns + router.urls
