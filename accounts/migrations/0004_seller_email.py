# Generated by Django 2.2.2 on 2019-06-27 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20190627_1803'),
    ]

    operations = [
        migrations.AddField(
            model_name='seller',
            name='email',
            field=models.EmailField(default='Jackie@gmail.com', max_length=254),
            preserve_default=False,
        ),
    ]
