# Generated by Django 2.0.3 on 2018-10-15 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0014_auto_20181011_1307'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='in_cart',
            field=models.BooleanField(default=True),
        ),
    ]