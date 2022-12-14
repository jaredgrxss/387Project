# Generated by Django 4.1.2 on 2022-10-26 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='date_posted',
            new_name='date_listed',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='price',
            new_name='min_price',
        ),
        migrations.AddField(
            model_name='item',
            name='highest_bid',
            field=models.IntegerField(default=0),
        ),
    ]
