# Generated by Django 4.2 on 2024-12-12 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0012_alter_paymentofpaypal_card_exp_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymentofpaypal',
            name='card_exp_date',
            field=models.CharField(max_length=10),
        ),
    ]
