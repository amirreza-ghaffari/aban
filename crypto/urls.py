from django.urls import path, include

app_name = "crypto"

urlpatterns = [
    path('api/v1/', include('crypto.api.v1.urls')),

]