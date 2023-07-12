from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length = 150)
    libelle = models.TextField()



class CustomUser(AbstractUser):
    user_type_data=((1,"HOD"),(2,"Staff"),(3,"Vigil"))
    user_type=models.CharField(default=1,choices=user_type_data,max_length=10)

class AdminHOD(models.Model):
    id=models.AutoField(primary_key=True)
    admin=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()

class Staff(models.Model):

    id=models.AutoField(primary_key=True)
    admin=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    address=models.TextField()
    phone_number= models.CharField(max_length = 150)
    nationality= models.CharField(max_length = 150)
    profile_pic=models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=200)
    salary=models.IntegerField()
    status= models.CharField(max_length = 150, default=1, null=True)
    department_id=models.ForeignKey(Department,on_delete=models.DO_NOTHING)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()



class Vigil(models.Model):
    id=models.AutoField(primary_key=True)
    admin=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    address=models.TextField()
    profile_pic=models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=200)
    phone_number= models.CharField(max_length = 150)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()












@receiver(post_save,sender=CustomUser)
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        if instance.user_type==1:
            AdminHOD.objects.create(admin=instance)
        if instance.user_type==2:
            Staff.objects.create(admin=instance,department_id=Department.objects.get(id=1),address="",salary=0,nationality="",phone_number="",profile_pic="", status=1)
        if instance.user_type==3:
            Vigil.objects.create(admin=instance,address="",profile_pic="",phone_number="")

@receiver(post_save,sender=CustomUser)
def save_user_profile(sender,instance,**kwargs):
    if instance.user_type==1:
        instance.adminhod.save()
    if instance.user_type==2:
        instance.staff.save()
    if instance.user_type==3:
        instance.vigil.save()        