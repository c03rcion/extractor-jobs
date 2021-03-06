# Generated by Django 2.2.9 on 2020-02-13 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0021_job_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='salary',
            new_name='high_salary',
        ),
        migrations.RenameField(
            model_name='job',
            old_name='salary_frequency',
            new_name='high_salary_frequency',
        ),
        migrations.AddField(
            model_name='job',
            name='low_salary',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='Two decimal places. Ex. 65,200.23', max_digits=15, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='low_salary_frequency',
            field=models.CharField(blank=True, choices=[('HR', 'Per-Hour'), ('DAY', 'Daily'), ('WEEK', 'Weekly'), ('MONTH', 'Monthly'), ('YEAR', 'Yearly')], max_length=225, null=True),
        ),
    ]
