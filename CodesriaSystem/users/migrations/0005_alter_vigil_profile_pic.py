# Generated by Django 4.2.3 on 2023-07-11 20:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0004_alter_staff_profile_pic"),
    ]

    operations = [
        migrations.AlterField(
            model_name="vigil",
            name="profile_pic",
            field=models.ImageField(max_length=200, upload_to=None),
        ),
    ]
