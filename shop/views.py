from django.shortcuts import render,get_object_or_404, redirect
from django.urls import reverse
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

from .models import Product, Checkout, CartItem

# Create your views here.



def home(request):
    #search
    is_home = request.resolver_match.url_name == 'home'
    product_qs = Product.objects.all().order_by('-id')
    item_name = request.GET.get('item_name')
    if item_name != '' and item_name is not None:
        product_qs = Product.objects.filter(title__icontains = item_name)
    
    #paginator
    paginator = Paginator(product_qs,8)
    page = request.GET.get('page')
    product_qs = paginator.get_page(page)
    return render(request, 'shop/home.html', context = {'product_qs': product_qs,'is_home':is_home})



def detail_view(request, id = None):
    is_detail = request.resolver_match.url_name == 'detail'
    obj = get_object_or_404(Product, id = id)
    return render(request, 'shop/detail.html', context = {'obj': obj, 'is_detail':is_detail})


@login_required
def checkout(request):
    # if not request.user.is_authenticated:
    #     return redirect(reverse('accounts:login/next=?checkout/'))

    if request.method == 'POST': 
        items = request.POST.get('items')
        last_name = request.POST.get('last-name')
        address = request.POST.get('address')
        address_2 = request.POST.get('address2')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zip = request.POST.get('zip')
        total = request.POST.get('total')
        Checkout.objects.create(items=items,customer= request.user,
                            last_name=last_name,address=address,address_2=address_2,
                            city=city,state=state,zip=zip,total=total)
        
   
    return render(request, 'shop/checkout.html')


