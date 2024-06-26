# Generated by Django 4.2.1 on 2023-07-06 12:50

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_type', models.CharField(choices=[('PERSONAL', 'PERSONAL'), ('INDIVIDUAL', 'INDIVIDUAL')], default='INDIVIDUAL', max_length=100, verbose_name='Customer Type')),
                ('salutation', models.CharField(choices=[('Mr.', 'Mr.'), ('Mrs.', 'Mrs.'), ('Miss', 'Miss'), ('Ms.', 'Ms.'), ('Dr.', 'Dr.')], max_length=20)),
                ('company_name', models.CharField(max_length=100, verbose_name='Company Name')),
                ('display_name', models.CharField(max_length=100, verbose_name='Display Name')),
                ('currency', models.CharField(choices=[('Eur', 'EUR'), ('NGN', 'NGN'), ('USD', 'USD')], max_length=100, verbose_name='Currency')),
                ('email', models.EmailField(max_length=254)),
                ('personal_phone', models.CharField(max_length=11, verbose_name='Personal Phone')),
                ('work_phone', models.CharField(max_length=11, verbose_name='Work Phone')),
            ],
        ),
        migrations.CreateModel(
            name='CustomerShippingAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=150, verbose_name='Street Address')),
                ('city', models.CharField(max_length=50, verbose_name='City')),
                ('state', models.CharField(max_length=50, verbose_name='State')),
                ('zip_code', models.CharField(max_length=50, verbose_name='Zip Code')),
                ('phone', models.CharField(max_length=11, verbose_name='Phone')),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('customer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='customers.customer')),
            ],
        ),
        migrations.CreateModel(
            name='CustomerBillingAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=150, verbose_name='Street Address')),
                ('city', models.CharField(max_length=50, verbose_name='City')),
                ('state', models.CharField(max_length=50, verbose_name='State')),
                ('zip_code', models.CharField(max_length=50, verbose_name='Zip Code')),
                ('phone', models.CharField(max_length=11, verbose_name='Phone')),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('customer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='customers.customer')),
            ],
        ),
    ]
