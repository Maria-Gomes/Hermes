from django.urls import path, include
from .views import add_subscription

urlpatterns = [
    path('new_subscription/<str:company_id>/', add_subscription),
]