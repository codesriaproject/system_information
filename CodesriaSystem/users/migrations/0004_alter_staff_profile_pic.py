# Generated by Django 4.2.3 on 2023-07-11 20:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0003_remove_secretaire_admin_remove_vigil_nationality_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="staff",
            name="profile_pic",
            field=models.ImageField(max_length=200, upload_to=None),
        ),
    ]