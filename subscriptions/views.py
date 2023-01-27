from .models import Subscription
from users.models import Company, PhoneNumber
from users.serializers import CompanySerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from datetime import date, timedelta


@api_view(['POST'])
def add_subscription(request, company_id):
    if request.method == 'POST':
        company = Company.objects.get(company_id=company_id)
        company_serializer = CompanySerializer(instance=company)
        expiry_date = date.today() + timedelta(days=30)
        data = {'company': company, 
                'type': request.data['type'], 
                'subscription_status': request.data['subscription_status'], 
                'expiry_date': expiry_date
                }
        subscription = Subscription.objects.create(**data)
        subscription.save()
        numbers = PhoneNumber.objects.filter(company_id=company_id)
        numbers.update(number_status='Active')
        return Response(company_serializer.data, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def make_payment(request, company_id):
    company = Company.objects.get(company_id=company_id)
    subscription = Subscription.objects.get(company=company)
    subscription.subscription_status = "Paid"
    subscription.expiry_date = date.today() + timedelta(days=1)
    subscription.save()
    numbers = PhoneNumber.objects.filter(company_id=company_id)
    numbers.update(number_status="Active")
    company_serializer = CompanySerializer(instance=company)
    return Response(company_serializer.data, status=status.HTTP_200_OK)