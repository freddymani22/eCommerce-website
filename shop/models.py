from django.urls import reverse
from django.db import models
from django.conf import settings


User = settings.AUTH_USER_MODEL



# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField()
    discount = models.FloatField()
    category = models.CharField(max_length=200)
    description =models.TextField()
    image = models.CharField(max_length=300)


    def __str__(self):
        return self.title
    

    def get_absolute_url(self):
        return reverse('shop:detail', kwargs={'id': self.id})




class Checkout(models.Model):
    customer = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    last_name = models.CharField(max_length=100,blank=True, null=True)
    mobile = models.IntegerField()
    address = models.CharField(max_length=200, null=False, blank=False)
    address_2 = models.CharField(max_length=200)
    city = models.CharField(max_length=100, null=False,blank=False)
    state = models.CharField(max_length=100, null=False, blank=False)
    zip = models.IntegerField(null=False, blank=False)
    total = models.FloatField(default=1)
    razor_pay_order_id = models.CharField(max_length=100, blank=True, null=True)
    razor_pay_payment_id = models.CharField(max_length=100, blank=True, null=True)
    razor_pay_payment_signature = models.CharField(max_length=100, blank=True, null=True)


class CartItem(models.Model):
    customer = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)


    @property
    def total_cost(self):
        return self.quantity * self.product.discount