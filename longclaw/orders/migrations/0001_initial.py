# Generated by Django 2.1.4 on 2018-12-22 14:48

from django.db import migrations, models
from django.conf import settings
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        (settings.PRODUCT_VARIANT_MODEL.split(".")[0], '__first__'),
        ('shipping', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_date', models.DateTimeField(blank=True, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.IntegerField(choices=[(1, 'Submitted'), (2, 'Fulfilled'), (3, 'Cancelled'), (4, 'Refunded'), (5, 'Payment Failed')], default=1)),
                ('status_note', models.CharField(blank=True, max_length=128, null=True)),
                ('transaction_id', models.CharField(blank=True, max_length=256, null=True)),
                ('email', models.EmailField(blank=True, max_length=128, null=True)),
                ('ip_address', models.GenericIPAddressField(blank=True, null=True)),
                ('shipping_rate', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('billing_address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='orders_billing_address', to='shipping.Address')),
                ('shipping_address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='orders_shipping_address', to='shipping.Address')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='orders.Order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.PRODUCT_VARIANT_MODEL)),
            ],
        ),
    ]
