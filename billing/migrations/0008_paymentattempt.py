# Generated by Django 4.1.5 on 2023-01-28 20:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0004_remove_company_payment_failed_and_more'),
        ('billing', '0007_delete_paymentattempt'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentAttempt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('amount', models.IntegerField()),
                ('failed', models.BooleanField(default=False)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='companies.company')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='billing.stripecustomer')),
            ],
        ),
    ]