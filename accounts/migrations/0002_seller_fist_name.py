# Generated by Django 2.2.2 on 2019-06-27 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='seller',
            name='fist_name',
            field=models.CharField(default='Jame', max_length=255),
            preserve_default=False,
        ),
    ]