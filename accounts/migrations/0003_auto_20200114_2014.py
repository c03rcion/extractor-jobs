# Generated by Django 2.2.5 on 2020-01-15 04:14

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20200112_2314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='siteuser',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, help_text='Format: +(country-code)(number) Ex. +12034578888', max_length=128, region=None),
        ),
    ]
