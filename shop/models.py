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
    items = models.CharField(max_length=1000)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    address_2 = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip = models.IntegerField()
    total = models.FloatField(default=1)


