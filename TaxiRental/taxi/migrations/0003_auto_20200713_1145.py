# Generated by Django 3.0.2 on 2020-07-13 06:15

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taxi', '0002_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='destination',
            field=models.CharField(choices=[('Panbazaar', 'Panbazaar'), ('Jalukbari', 'Jalukbari'), ('Airport', 'Airport'), ('PaltanBazaar', 'PaltanBazaar'), ('GS Road', 'GS Road'), ('Maligaon', 'Maligaon')], default='Panbazaar', max_length=50),
        ),
        migrations.AlterField(
            model_name='order',
            name='phone_no',
            field=models.CharField(max_length=10, validators=[django.core.validators.RegexValidator('^[0-9]*$', 'Only numeric characters are allowed.')]),
        ),
    ]