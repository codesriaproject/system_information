# Generated by Django 4.2.3 on 2023-07-19 13:30

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("users", "0005_alter_vigil_profile_pic"),
    ]

    operations = [
        migrations.CreateModel(
            name="Fournisseur",
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
                ("name", models.CharField(max_length=150)),
                ("address", models.TextField(default="", null=True)),
                (
                    "phone_number",
                    models.CharField(default="", max_length=150, null=True),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Voucher",
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
            ],
        ),
        migrations.CreateModel(
            name="StaffLeave",
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
                ("note_demande", ckeditor.fields.RichTextField()),
                ("date_demande", models.DateTimeField(auto_now_add=True, null=True)),
                (
                    "chef_recept",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="chef_rept",
                        to="users.staff",
                    ),
                ),
                (
                    "staff",
                    models.ForeignKey(
                        default=1,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        to="users.staff",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="SecretaryValidate",
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
                ("signature", models.ImageField(default="", null=True, upload_to="")),
                (
                    "purchase_recept",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="users.staff"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Invoice",
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
                (
                    "total",
                    models.DecimalField(
                        decimal_places=2, default=0, max_digits=1000, null=True
                    ),
                ),
                ("date_creation", models.DateTimeField(auto_now_add=True, null=True)),
                ("lieu_livraison", models.TextField(default="", null=True)),
                ("observation", models.TextField(default="", null=True)),
                ("status", models.SmallIntegerField(default=0, null=True)),
                (
                    "client",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="purchase.fournisseur",
                    ),
                ),
                (
                    "staffleave",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="staff_leave",
                        to="purchase.staffleave",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Article",
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
                ("name", models.CharField(max_length=32)),
                ("quantity", models.IntegerField()),
                ("unit_price", models.DecimalField(decimal_places=2, max_digits=1000)),
                ("total", models.DecimalField(decimal_places=2, max_digits=1000)),
                (
                    "invoice",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="purchase.invoice",
                    ),
                ),
            ],
            options={
                "verbose_name": "Article",
                "verbose_name_plural": "Articles",
            },
        ),
    ]