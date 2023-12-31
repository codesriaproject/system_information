# Generated by Django 4.2.3 on 2023-07-21 11:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0006_signature"),
        ("purchase", "0005_secretaryvalidate_staff"),
    ]

    operations = [
        migrations.AlterField(
            model_name="secretaryvalidate",
            name="staff",
            field=models.ForeignKey(
                default=5,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="users.staff",
            ),
        ),
    ]
