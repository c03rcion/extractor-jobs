# Generated by Django 2.2.5 on 2020-01-16 05:34

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('jobs', '0019_auto_20200115_1806'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='jobs_liked', to=settings.AUTH_USER_MODEL),
        ),
    ]