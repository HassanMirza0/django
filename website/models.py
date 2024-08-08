from django.db import models
from django.contrib.auth.models import User

from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField
# Create your models here.

from django import forms




class Contactus(models.Model):
     user=models.ForeignKey(User, on_delete=models.SET_NULL,null=True,blank=True)
     name=models.CharField(max_length=112 ,blank=False,null=False)
     email=models.CharField(max_length=12)
     password=models.CharField(max_length=12)
     phoneNo=models.CharField(max_length=12 )
     date=models.DateField()

     
     def __str__(self):
       return self.name


class Product(models.Model):
    product_id=models.AutoField
    product_title=models.CharField(max_length=50 , default="")
    name=models.CharField(max_length=50)
    brand_name=models.CharField(max_length=50 ,default="")
    price=models.FloatField(default=0)
    desc=RichTextField(null="true")
    sub_desc=RichTextField(null="true")
    add_info=RichTextField(null="true")
    pub_date=models.DateField()
    image= models.ImageField(upload_to="static/images",default="")     



    def __str__(self):
       return self.name
    

    
class Order(models.Model):
     user=models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
     first_name=models.CharField(max_length=112)
     last_name=models.CharField(max_length=112)
     email=models.EmailField(max_length=102)
     address=models.TextField()
     phoneNo=models.CharField( max_length=50)
     houseno=models.CharField( max_length=50)
     postcode=models.CharField( max_length=50)
     payment_id=models.CharField(max_length=300,null=True,blank=True)
     paid=models.BooleanField(default=False,null=True)
     amount=models.CharField(max_length=12 )
     date=models.DateField(auto_now_add=True)

     
     def __str__(self):
       return self.user.username
     

        
class OrderItem(models.Model):
     order=models.ForeignKey(Order, on_delete=models.CASCADE,null=True,blank=True)
     Product=models.CharField(max_length=212)
     image=models.ImageField(upload_to="static/images/order_img")
     quantity=models.CharField(max_length=50)
     price=models.CharField(max_length=50)
     total=models.CharField(max_length=1000)

       
     def __str__(self):
       return self.order.user.username
     
