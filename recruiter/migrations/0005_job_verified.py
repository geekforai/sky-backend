# Generated by Django 4.0.6 on 2024-01-28 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recruiter', '0004_job_employer_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='verified',
            field=models.CharField(default='no', max_length=10),
            preserve_default=False,
        ),
    ]