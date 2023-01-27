from django.urls import path, include
from .views import company_list, numbers_list, new_user, create_phone_number

urlpatterns = [
    path('companies/', company_list),
    path('new_user/', new_user),
    path('<str:company_id>/add_number/', create_phone_number),
    path('<str:company_id>/numbers', numbers_list)
]