from django.db import models
from users.models import *
from django_countries.fields import CountryField
# Create your models here.


class Status(models.Model):
    name = models.CharField(max_length = 150)
    


class Directory(models.Model):
    name = models.CharField(max_length = 150)
    surname = models.CharField(max_length = 150)
    countries = CountryField()
    gender = models.CharField(max_length = 150)
    email=models.EmailField(unique=True, null=True, default="noreply@codesria.org")
    phone_number = models.CharField(max_length = 150, null=True, default="")
    biography = models.TextField(default="not biography", null=True)
    bibliography = models.TextField(default="not bibliography", null=True)
    orcid = models.CharField(max_length = 150, default="not orcid", null=True)
    affliation = models.CharField(max_length = 150, default="not affliation", null=True)
    status=models.ForeignKey(Status, on_delete=models.PROTECT, null=True, default=1)



    

    
    
    
    

    
    
    
    
    





