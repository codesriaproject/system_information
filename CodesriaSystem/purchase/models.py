from django.db import models
from users.models import *
from ckeditor.fields import RichTextField
# Create your models here.


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


    @property
    def get_total(self):
        articles = self.article_set.all()   
        total = sum(article.get_total for article in articles)
        return total    
    
    






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
    pass



    

    
    
    


