# Generated by Django 4.1.5 on 2023-01-18 13:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_remove_company_name_alter_phonenumber_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phonenumber',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='numbers', to='users.company'),
        ),
    ]
