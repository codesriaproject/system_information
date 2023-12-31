# Generated by Django 4.2.3 on 2023-07-12 22:51

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):
    dependencies = [
        ("directory", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="directory",
            name="affliation",
            field=models.CharField(default="not affliation", max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name="directory",
            name="bibliography",
            field=models.TextField(default="not bibliography", null=True),
        ),
        migrations.AlterField(
            model_name="directory",
            name="biography",
            field=models.TextField(default="not biography", null=True),
        ),
        migrations.AlterField(
            model_name="directory",
            name="countries",
            field=django_countries.fields.CountryField(max_length=2),
        ),
        migrations.AlterField(
            model_name="directory",
            name="orcid",
            field=models.CharField(default="not orcid", max_length=150, null=True),
        ),
    ]
