# Generated by Django 4.1.5 on 2023-01-18 07:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_company_company_id_phonenumber'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='name',
        ),
        migrations.AlterField(
            model_name='phonenumber',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='phone_numbers', to='users.company'),
        ),
    ]