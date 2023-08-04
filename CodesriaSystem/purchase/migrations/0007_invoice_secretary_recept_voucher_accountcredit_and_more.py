# Generated by Django 4.2.3 on 2023-07-25 09:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0006_signature"),
        ("purchase", "0006_alter_secretaryvalidate_staff"),
    ]

    operations = [
        migrations.AddField(
            model_name="invoice",
            name="secretary_recept",
            field=models.ForeignKey(
                default=2,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="secretary_rept",
                to="users.staff",
            ),
        ),
        migrations.AddField(
            model_name="voucher",
            name="accountcredit",
            field=models.DecimalField(
                decimal_places=2, default=0, max_digits=1000, null=True
            ),
        ),
        migrations.AddField(
            model_name="voucher",
            name="accountdebit",
            field=models.DecimalField(
                decimal_places=2, default=0, max_digits=1000, null=True
            ),
        ),
        migrations.AddField(
            model_name="voucher",
            name="bankname",
            field=models.CharField(default="", max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="voucher",
            name="budgetyear",
            field=models.DecimalField(
                decimal_places=2, default=0, max_digits=1000, null=True
            ),
        ),
        migrations.AddField(
            model_name="voucher",
            name="chequetransfert",
            field=models.CharField(default="", max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="voucher",
            name="date_prepared",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name="voucher",
            name="description",
            field=models.TextField(default="", null=True),
        ),
        migrations.AddField(
            model_name="voucher",
            name="donor",
            field=models.CharField(default="", max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="voucher",
            name="lieu_livraison",
            field=models.TextField(default="", null=True),
        ),
        migrations.AddField(
            model_name="voucher",
            name="programmeactivecode",
            field=models.CharField(default="", max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="voucher",
            name="programmeactivetitle",
            field=models.CharField(default="", max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="voucher",
            name="programmecode",
            field=models.CharField(default="", max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="voucher",
            name="programmetype",
            field=models.CharField(default="", max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="voucher",
            name="secretary_recept",
            field=models.ForeignKey(
                default=2,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="secretary_recept",
                to="users.staff",
            ),
        ),
        migrations.AddField(
            model_name="voucher",
            name="signature",
            field=models.ForeignKey(
                default=1,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="users.signature",
            ),
        ),
        migrations.AddField(
            model_name="voucher",
            name="staffleave",
            field=models.ForeignKey(
                default=1,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="staff_leave_voucher",
                to="purchase.staffleave",
            ),
        ),
        migrations.AddField(
            model_name="voucher",
            name="status",
            field=models.SmallIntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name="voucher",
            name="subprogrammecode",
            field=models.CharField(default="", max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="voucher",
            name="total",
            field=models.DecimalField(
                decimal_places=2, default=0, max_digits=1000, null=True
            ),
        ),
    ]