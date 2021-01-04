from django.db import models
from django.forms import ModelForm

from accounts.models import User
# Create your models here.
from products.models import Product


class ShopCart(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    product=models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)
    quantity=models.IntegerField()

    def __str__(self):
        return self.product.title

    @property
    def amount(self):
        return (self.quantity * self.product.price)

    @property
    def price(self):
        return (self.product.price)


class ShopCartForm(ModelForm):
    class Meta:
        model = ShopCart
        fields = ['quantity']



class Order(models.Model):
    STATUS= (
        ('New', 'Yeni'),
        ('Accepted', 'Kabul Edildi'),
        ('Preparing', 'Hazırlanıyor'),
        ('OnShipping','Kargolandı'),
        ('Completed', 'Tamamlandı'),
        ('Canceled', 'Iptal'),
    )

    user=models.ForeignKey(User,on_delete=models.SET_NULL, null=True)
    first_name=models.CharField(max_length=15)
    last_name=models.CharField(max_length=20)
    phone=models.CharField(blank=True, max_length=20)
    total=models.FloatField()
    status=models.CharField(max_length=10,choices=STATUS,default='New')
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.first_name



class OrderForm(ModelForm):
    class Meta:
        model=Order
        fields=['first_name','last_name','phone']


class OrderProduct(models.Model):
    STATUS = (
        ('New', 'Yeni'),
        ('Accepted', 'Kabul Edildi'),
        ('Canceled', 'Iptal'),
    )
    order=models.ForeignKey(Order,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity=models.IntegerField()
    price=models.FloatField()
    amount=models.FloatField()
    status=models.CharField(max_length=10, choices=STATUS, default='New')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product.title







