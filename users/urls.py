from django.urls import path, include
from .views import company_list, numbers_list, new_user, create_phone_number, LoginView, UserView

urlpatterns = [
    path('companies/', company_list),
    path('new_user/', new_user),
    path('login/', LoginView.as_view()),
    path('user/', UserView.as_view()),
    path('<str:company_id>/add_number/', create_phone_number),
    path('<str:company_id>/numbers', numbers_list)
]