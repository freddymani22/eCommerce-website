from django.contrib import admin


from .models import Product
# Register your models here.

class ProductsAdmin(admin.ModelAdmin):
    list_display = ['id','title']
    search_fields = ['title']



admin.site.register(Product,ProductsAdmin)