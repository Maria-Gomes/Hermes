# Generated by Django 4.1.5 on 2023-01-20 15:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='expiry_date',
            field=models.DateField(default=datetime.date(2023, 1, 20)),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='status',
            field=models.CharField(choices=[('Paid', 'Paid'), ('Unpaid', 'Unpaid')], default='Unpaid', max_length=6),
        ),
    ]
