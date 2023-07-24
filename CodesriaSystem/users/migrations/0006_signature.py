# Generated by Django 4.2.3 on 2023-07-20 10:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0005_alter_vigil_profile_pic"),
    ]

    operations = [
        migrations.CreateModel(
            name="Signature",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("sign", models.ImageField(upload_to="")),
                (
                    "staff_sign",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="users.staff"
                    ),
                ),
            ],
        ),
    ]