# Generated by Django 5.0.1 on 2024-02-07 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("course", "0003_rename_corse_title_course_course_title_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="course",
            name="course_img",
            field=models.ImageField(blank=True, upload_to=""),
        ),
    ]
