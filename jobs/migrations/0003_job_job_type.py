# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2019-12-01 06:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_auto_20191130_2153'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='job_type',
            field=models.CharField(blank=True, choices=[('FT', 'Full-Time'), ('PT', 'Part-Time'), ('1099', 'Contract')], max_length=255, null=True),
        ),
    ]
