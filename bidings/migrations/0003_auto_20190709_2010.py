# Generated by Django 2.2.3 on 2019-07-09 20:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bidings', '0002_auto_20190708_0358'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bid',
            old_name='auction_id',
            new_name='product',
        ),
    ]