# Generated by Django 2.2.5 on 2019-11-27 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_example', '0005_computers_price_currency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='computers',
            name='comp_link',
            field=models.TextField(max_length=256),
        ),
        migrations.AlterField(
            model_name='computers',
            name='picture_link',
            field=models.ImageField(default='default.jpg', upload_to='comp_images'),
        ),
    ]
