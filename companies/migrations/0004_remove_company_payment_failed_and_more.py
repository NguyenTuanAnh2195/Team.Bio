# Generated by Django 4.1.5 on 2023-01-28 20:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0003_company_trial_days'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='payment_failed',
        ),
        migrations.RemoveField(
            model_name='company',
            name='payment_failed_count',
        ),
        migrations.RemoveField(
            model_name='company',
            name='payment_failed_date',
        ),
    ]