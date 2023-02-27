# Generated by Django 4.1.5 on 2023-02-18 07:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coupon_code', models.CharField(max_length=100)),
                ('coupon_limit', models.IntegerField(default=1)),
                ('discount_amt', models.IntegerField()),
                ('minimum_amt', models.IntegerField()),
                ('is_expired', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ReviewCoupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coupon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='coupon', to='cart.coupon')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='coupon_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]