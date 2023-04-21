from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator


from .models import Product

# Create your views here.



def home(request):
    #search
    product_qs = Product.objects.all().order_by('-id')
    item_name = request.GET.get('item_name')
    if item_name != '' and item_name is not None:
        product_qs = Product.objects.filter(title__icontains = item_name)
    
    #paginator
    paginator = Paginator(product_qs,4)
    page = request.GET.get('page')
    product_qs = paginator.get_page(page)
    return render(request, 'shop/home.html', context = {'product_qs': product_qs})



def detail_view(request, id = None):
    obj = get_object_or_404(Product, id = id)
    return render(request, 'shop/detail.html', context = {'obj': obj})


def checkout(request):
    return render(request, 'shop/checkout.html')