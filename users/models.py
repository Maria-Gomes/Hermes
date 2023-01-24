from django.db import models
from django.contrib.auth.models import User

class Company(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_id = models.CharField(unique=True, primary_key=True, max_length=14)

    def __str__(self):
        return f'{self.user.username}'

NUMBER_STATUS = [("Active", "Active"), ("Inactive", "Inactive")]

class PhoneNumber(models.Model):
    company = models.ForeignKey(Company, related_name='numbers', on_delete=models.CASCADE)
    number = models.CharField(unique=True, max_length=14)
    number_status = models.CharField(choices=NUMBER_STATUS, default="Inactive", max_length=8)
