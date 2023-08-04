from django.db import models
from reportlab.pdfbase.pdfform import textFieldAbsolute

from users.models import *

# Create your models here.

 


class InOutStaff(models.Model):
    staff = models.ForeignKey(Staff,on_delete=models.CASCADE)
    date=models.DateField(auto_now=False, auto_now_add=True)
    enter = models.TimeField(auto_now=False, auto_now_add=True, null=True)
    exit= models.TimeField(auto_now=False, auto_now_add=False,default="", null=True)
    comment=models.TextField(default="", null=True)
    






    
    
