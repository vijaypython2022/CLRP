# Generated by Django 4.2.2 on 2023-07-01 17:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0003_alter_customer_purchase_expiry_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='rewardpoints',
            name='expiry_date',
            field=models.DateField(default=datetime.date(2023, 9, 29)),
        ),
    ]