# Generated by Django 5.0.1 on 2024-02-16 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("course", "0004_alter_course_course_img"),
    ]

    operations = [
        migrations.AddField(
            model_name="course",
            name="price",
            field=models.IntegerField(default="499"),
            preserve_default=False,
        ),
    ]
