# Generated by Django 2.2.5 on 2019-09-08 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_example', '0004_remove_computers_price_currency'),
    ]

    operations = [
        migrations.AddField(
            model_name='computers',
            name='price_currency',
            field=models.CharField(default='P', max_length=1),
            preserve_default=False,
        ),
    ]
