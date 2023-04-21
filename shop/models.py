from django.urls import reverse

from django.db import models


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
