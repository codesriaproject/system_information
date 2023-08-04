from django.db import models
from users.models import *
from ckeditor.fields import RichTextField
# Create your models here.

from num2words import num2words


class Fournisseur(models.Model):
    name = models.CharField(max_length = 150)
    address = models.TextField(null=True, default="")
    phone_number = models.CharField(max_length = 150, null=True, default="")



class StaffLeave(models.Model):
    staff = models.ForeignKey(Staff,on_delete=models.PROTECT,null=True, default=1)
    note_demande = RichTextField()
    chef_recept=models.ForeignKey(Staff,on_delete=models.PROTECT, related_name="chef_rept")
    date_demande=models.DateTimeField(auto_now=False, auto_now_add=True, null=True)
    signature =models.ForeignKey(Signature, on_delete=models.PROTECT, null=True, default=1)


class Invoice(models.Model):
    staffleave=models.ForeignKey(StaffLeave, on_delete=models.CASCADE, related_name="staff_leave")
    client=models.ForeignKey(Fournisseur, on_delete=models.PROTECT)
    total = models.DecimalField(max_digits=1000, decimal_places=2,null=True, default=0)
    date_creation = models.DateTimeField(auto_now=False, auto_now_add=True,null=True, )
    lieu_livraison = models.TextField(null=True, default="")
    observation = models.TextField(null=True, default="")
    status = models.SmallIntegerField(default=0, null=True)
    signature =models.ForeignKey(Signature, on_delete=models.PROTECT, null=True, default=1)
    secretary_recept=models.ForeignKey(Staff,on_delete=models.PROTECT, related_name="secretary_rept", null=True, default=2)
    object= models.CharField(max_length=100,null=True, default="")
    marche = models.CharField(max_length=100,null=True, default="")
    modalitedepaiement=models.IntegerField(null=True, default=30)
    imputation=models.CharField(max_length=100,null=True, default="")
    date_livraison = models.DateTimeField(auto_now=False, auto_now_add=False,null=True)



    @property
    def get_total(self):
        articles = self.article_set.all()   
        total = sum(article.get_total for article in articles)
        return total

    def numwords(self):
        articles = self.article_set.all()
        total = sum(article.get_total for article in articles)

        return num2words(total, lang='fr')






class Article(models.Model):
    
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)

    name = models.CharField(max_length=32)

    quantity = models.IntegerField()

    unit_price = models.DecimalField(max_digits=1000, decimal_places=2)

    total = models.DecimalField(max_digits=1000, decimal_places=2)

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

    @property
    def get_total(self):
        total = self.quantity * self.unit_price   
        return total 
        



class SecretaryValidate(models.Model):
    purchase_recept=models.ForeignKey(Invoice,on_delete=models.CASCADE, null=True, default=0)
    signature =models.ForeignKey(Signature, on_delete=models.PROTECT, null=True, default=0)
    staff=models.ForeignKey(Staff,on_delete=models.CASCADE, null=True, default=5)


class Voucher(models.Model):
    staffleave = models.ForeignKey(StaffLeave, on_delete=models.CASCADE, related_name="staff_leave_voucher", null=True, default=1)
    date_prepared = models.DateTimeField(auto_now=False, auto_now_add=True, null=True)
    lieu_livraison = models.TextField(null=True, default="")
    status = models.SmallIntegerField(default=0, null=True)
    total = models.DecimalField(max_digits=1000, decimal_places=2,null=True, default=0)
    description = models.TextField(null=True, default="")
    chequetransfert=models.CharField(max_length=200, null=True, default="")
    bankname=models.CharField(max_length=200, null=True, default="")
    budgetyear=models.DecimalField(max_digits=1000, decimal_places=2, null=True, default=0)
    programmetype=models.CharField(max_length=200, null=True, default="")
    programmecode=models.CharField(max_length=200, null=True, default="")
    subprogrammecode=models.CharField(max_length=200, null=True, default="")
    programmeactivecode=models.CharField(max_length=200, null=True, default="")
    programmeactivetitle=models.CharField(max_length=200, null=True, default="")
    donor=models.CharField(max_length=200, null=True, default="")
    accountdebit=models.DecimalField(max_digits=1000, decimal_places=2, null=True, default=0)
    accountcredit=models.DecimalField(max_digits=1000, decimal_places=2, null=True, default=0)
    signature =models.ForeignKey(Signature, on_delete=models.PROTECT, null=True, default=1)
    secretary_recept=models.ForeignKey(Staff,on_delete=models.PROTECT, related_name="secretary_recept", null=True, default=2)
    client=models.ForeignKey(Fournisseur, on_delete=models.PROTECT, null=True, default=1000)
















    

    
    
    


