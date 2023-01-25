from django.http import JsonResponse
from django.contrib.auth.models import User
from .models import Company, PhoneNumber
from subscriptions.models import Subscription
from .serializers import CompanySerializer, NumberSerializer, UserSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed
import jwt, secrets, datetime

def company_list(request):
    companies = Company.objects.all()
    serializer = CompanySerializer(companies, many=True)
    return JsonResponse({"companies": serializer.data})

@api_view(['POST'])
def new_user(request):
    if request.method == 'POST':
        user_serializer = UserSerializer(data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            company_id = generate_number()
            user = user_serializer.instance.id
            company_serializer = CompanySerializer(data={'user': user, 'company_id': company_id, 'numbers': [{'number': company_id, 'number_status': 'Inactive'}]})
            if company_serializer.is_valid():
                company = company_serializer.save()
                data = {'company': company, 'number': company_id, 'number_status': 'Inactive'}
                number = PhoneNumber.objects.create(**data)
                number.save()
                return Response(company_serializer.data, status=status.HTTP_201_CREATED)
            else:
                print(company_serializer.errors)

@api_view(['POST'])
def create_phone_number(request, company_id):
    if request.method == 'POST':
        number = generate_number()
        company = Company.objects.get(company_id=company_id)
        number_status = "Inactive"
        if Subscription.objects.filter(company=company).exists():
            if Subscription.objects.get(company=company).subscription_status == "Paid":
                number_status = "Active"
        company_serializer = CompanySerializer(instance=company)
        data = {'company': company, 'number': number, 'number_status': number_status}
        new_phone_number = PhoneNumber.objects.create(**data)
        new_phone_number.save()
        return Response(company_serializer.data, status=status.HTTP_201_CREATED)

def generate_number():
    number = secrets.choice(range(10000000, 99999999))
    if(PhoneNumber.objects.filter(company_id = number).exists()):
        generate_number()
    return number

class LoginView(APIView):
    def post(self, request):
        username = request.data['username']
        password = request.data['password']
        user = User.objects.filter(username=username).first()
        
        if user is None:
            raise AuthenticationFailed("User not found.")
        if not user.check_password(password):
            raise AuthenticationFailed("Incorrect Password.")

        payload = {
            "id": user.id,
            "exp": datetime.datetime.utcnow()+ datetime.timedelta(minutes=90),
            "iat": datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret', algorithm="HS256").decode("utf-8")
        response = Response()
        response.set_cookie(key="jwt", value=token, httponly=True)
        response.data = {"jwt": token}

        return response

class UserView(APIView):
    def get(self, request):
        token = request.COOKIES.get("jwt")
        
        if not token:
            raise AuthenticationFailed("Unauthenticated User")

        try:
            payload = jwt.decode(token, 'secret', algorithm=["HS256"])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed("Unauthenticated User")

        user = User.objects.filter(id=payload['id']).first()
        serializer = UserSerializer(user)

        return Response(serializer.data, status=status.HTTP_200_OK)


def numbers_list(request, company_id):
    numbers = PhoneNumber.objects.filter(company_id = company_id)
    serializer = NumberSerializer(numbers, many=True)
    return JsonResponse({"phone numbers": serializer.data})

