from django.urls import path, include
from .views import add_subscription, make_payment

urlpatterns = [
    path('new_subscription/<str:company_id>/', add_subscription),
    path('pay/<str:company_id>/', make_payment),
]