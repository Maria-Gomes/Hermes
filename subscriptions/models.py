from django.db import models
from users.models import Company
from datetime import date


SUBSCRIPTION_TYPE = [("Gold", "Gold"), ("Silver", "Silver"), ("Bronze", "Bronze")]
SUBSCRIPTION_STATUS = [("Paid", "Paid"), ("Unpaid", "Unpaid")]

class Subscription(models.Model):
    company = models.OneToOneField(Company, related_name='subscription', on_delete=models.CASCADE)
    type = models.CharField(choices=SUBSCRIPTION_TYPE, max_length=6)
    subscription_status = models.CharField(choices=SUBSCRIPTION_STATUS, default="Unpaid", max_length=6)
    expiry_date = models.DateField(default=date.today())

    def __str__(self):
        return f'{self.type}'