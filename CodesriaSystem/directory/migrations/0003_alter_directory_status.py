# Generated by Django 4.2.3 on 2023-07-13 13:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("directory", "0002_alter_directory_affliation_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="directory",
            name="status",
            field=models.ForeignKey(
                default=1,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="directory.status",
            ),
        ),
    ]
