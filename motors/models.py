from django.db import models
from accounts.models import User

class Products(models.Model):
    brand_name=models.CharField(max_length=50)
    choices_type=(
    ('Personal','Personal'),
    ('Nissan','Nissan'),
    ('Lorry','Lorry'),
    ('Bus','Bus')
    )
    type=models.CharField(max_length=20,choices=choices_type,blank=True,null=True)
    category_choices=(
    ('New','New'),
    ('Refurbished','Refurbished'),
    ('Other','Other')
    )
    category=models.CharField(max_length=30,choices=category_choices,blank=True,null=True)
    image=models.ImageField(upload_to="day/motors")
    price=models.FloatField(default=0.00)
    owners_phone=models.CharField(max_length=30,blank=True,null=True)
    owners_email=models.EmailField(max_length=30,blank=True,null=True)
    date_added=models.DateField(auto_now_add=True)
    date_updated=models.DateField(auto_now=True)
    sold=models.BooleanField(default=False)
    description=models.TextField(blank=True,null=True)

    def __str__(self):
        return self.brand_name

    class Meta:
        verbose_name_plural='Products'
class Wish_Product(models.Model):
    wish_brand=models.ForeignKey(Products,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    sold=models.BooleanField(default=False)

    def __str__(self):
        return self.wish_brand.brand_name
    class Meta:
        verbose_name_plural='Wish_Product'

class WishList(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    wish_date=models.DateField(auto_now_add=True)
    sold=models.BooleanField(default=False)
    wish_brands=models.ManyToManyField(Wish_Product,verbose_name="Brand Name")

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural='WishList'
