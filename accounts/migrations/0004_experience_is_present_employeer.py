# Generated by Django 2.2.8 on 2020-02-06 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20200114_2014'),
    ]

    operations = [
        migrations.AddField(
            model_name='experience',
            name='is_present_employeer',
            field=models.BooleanField(default=False),
        ),
    ]
