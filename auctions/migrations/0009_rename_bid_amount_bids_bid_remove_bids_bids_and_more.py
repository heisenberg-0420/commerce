# Generated by Django 4.1.3 on 2022-11-22 20:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0008_alter_bids_bid_amount'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bids',
            old_name='bid_amount',
            new_name='bid',
        ),
        migrations.RemoveField(
            model_name='bids',
            name='bids',
        ),
        migrations.AlterField(
            model_name='bids',
            name='bidder',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bid', to=settings.AUTH_USER_MODEL),
        ),
    ]
