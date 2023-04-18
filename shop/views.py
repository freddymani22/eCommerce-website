from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator


from .models import Product

# Create your views here.


@login_required
def home(request):
    #search
    product_qs = Product.objects.all()
    item_name = request.GET.get('item_name')
    if item_name != '' and item_name is not None:
        product_qs = Product.objects.filter(title__icontains = item_name)
    
    #paginator
    paginator = Paginator(product_qs,4)
    page = request.GET.get('page')
    product_qs = paginator.get_page(page)
    return render(request, 'shop/home.html', context = {'product_qs': product_qs})