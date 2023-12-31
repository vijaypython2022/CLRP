# Generated by Django 4.2.2 on 2023-06-28 18:04

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('mobile', models.IntegerField()),
                ('address', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Membership_tiers',
            fields=[
                ('tier', models.CharField(choices=[('silver', 'Silver'), ('gold', 'Gold'), ('platinum', 'Platinum')], max_length=10, primary_key=True, serialize=False)),
                ('requirement', models.CharField(max_length=100)),
                ('discount', models.IntegerField()),
                ('benifits', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.CharField(max_length=10, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('desc', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('vid', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('mobile', models.IntegerField()),
                ('address', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='RewardPoints',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('points', models.IntegerField(default=0)),
                ('last_updated', models.DateTimeField(auto_now_add=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Api.customer')),
            ],
        ),
        migrations.CreateModel(
            name='RedemptionRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=100)),
                ('returned_date', models.DateField()),
                ('status', models.CharField(choices=[('Returned', 'Returned'), ('Pending', 'Pending')], default='Pending', max_length=10)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PurchaseReturn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('return_quantity', models.PositiveIntegerField()),
                ('return_reason', models.CharField(max_length=100)),
                ('return_date', models.DateField(auto_now_add=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Api.customer')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Api.product')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='vendor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Api.vendor'),
        ),
        migrations.CreateModel(
            name='LoyaltyProgram',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=250)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('membership_tier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Api.membership_tiers')),
            ],
        ),
        migrations.CreateModel(
            name='Customer_purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('purchase_date', models.DateField(auto_now_add=True)),
                ('expiry_date', models.DateField(default=datetime.date(2023, 9, 26))),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Api.customer')),
                ('loyaltyProgram', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Api.loyaltyprogram')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Api.product')),
            ],
        ),
        migrations.AddField(
            model_name='customer',
            name='membership',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Api.membership_tiers'),
        ),
        migrations.AddField(
            model_name='customer',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
