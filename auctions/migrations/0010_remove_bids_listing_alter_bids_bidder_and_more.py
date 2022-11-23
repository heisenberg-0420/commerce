# Generated by Django 4.1.3 on 2022-11-23 21:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0009_rename_bid_amount_bids_bid_remove_bids_bids_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bids',
            name='listing',
        ),
        migrations.AlterField(
            model_name='bids',
            name='bidder',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bidder', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='listings',
            name='price',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bid_price', to='auctions.bids'),
        ),
    ]
