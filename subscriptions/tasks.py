from datetime import date
from django_q.tasks import Schedule

def check_subscription_status():
    print(date.today())

Schedule.objects.create(func='check_subscription_status', minutes=1, repeats=-1)