# Generated by Django 2.2.3 on 2019-07-10 07:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bidings', '0006_bid_bid_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bid',
            name='bid_id',
        ),
    ]