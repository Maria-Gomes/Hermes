from rest_framework import serializers
from .models import Subscription
from users.models import Company

class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ['type', 'subscription_status', 'expiry_date']