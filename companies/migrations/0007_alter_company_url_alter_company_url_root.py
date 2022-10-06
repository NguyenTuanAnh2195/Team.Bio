# Generated by Django 4.1.2 on 2022-10-06 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0006_company_url_root_alter_company_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='url',
            field=models.URLField(unique=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='url_root',
            field=models.CharField(max_length=250, unique=True),
        ),
    ]
