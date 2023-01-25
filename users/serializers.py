from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Company, PhoneNumber
from subscriptions.models import Subscription
from subscriptions.serializers import SubscriptionSerializer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

        def create(self, validated_data):
            print(validated_data)
            password = validated_data.pop('password')
            user = User.objects.create_user(validated_data['username'], validated_data['password'])
            user.set_password(password)
            user.save()

class NumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhoneNumber
        fields = ['number', 'number_status']


class CompanySerializer(serializers.ModelSerializer):
    numbers = NumberSerializer(many=True, read_only=True)
    subscription = SubscriptionSerializer(read_only=True)

    class Meta:
        model = Company
        fields = ['user', 'company_id', 'numbers', 'subscription']

        def create(self, validated_data):
            company = Company.objects.create(**validated_data)
            return company

