# Generated by Django 2.2.3 on 2019-07-08 03:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0003_listing_deadline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='seller',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='accounts.Seller'),
        ),
    ]