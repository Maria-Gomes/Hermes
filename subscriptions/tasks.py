from datetime import date
from subscriptions.models import Subscription
from users.models import Company, PhoneNumber
from django_q.tasks import Schedule

def check_payment():
    expired_subscriptions = Subscription.objects.filter(expiry_date__lte=date.today())
    expired_subscriptions.update(subscription_status="Unpaid")
    for subscription in expired_subscriptions:
        company = Company.objects.get(company_id = subscription.company.company_id)
        numbers = PhoneNumber.objects.filter(company_id = company.company_id)
        numbers.update(number_status="Inactive")
    print("Checking done")

# Schedule.objects.create(name="check payments", func='subscriptions.tasks.check_payment', schedule_type=Schedule.MINUTES, minutes=1, repeats=-1)