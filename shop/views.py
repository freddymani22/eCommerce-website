from django.shortcuts import render,get_object_or_404, redirect
from django.urls import reverse
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
import razorpay
from django.conf import settings
from django.contrib import messages

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
        last_name = request.POST.get('last-name')
        mobile = request.POST.get('number')
        address = request.POST.get('address')
        address_2 = request.POST.get('address2')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zip = request.POST.get('zip')
        total = request.POST.get('total')
        data = {'mobile':mobile,"last_name":last_name,'address':address,'address_2':address_2,'city':city,'state':state,'zip':zip,'total':total}
        Checkout.objects.update_or_create(customer= request.user,defaults= data)
        return redirect('shop:summary')
       
   
    
    return render(request, 'shop/checkout.html')


def order_summary(request):
    cart_qs = CartItem.objects.filter(customer= request.user)
    checkout_details = Checkout.objects.get(customer = request.user)
    client = razorpay.Client(auth=(settings.KEY, settings.SECRET ))
    payment = client.order.create({'amount': 1000, 'currency':"INR", 'payment_capture':1})
   
    client = razorpay.Client(auth=(settings.KEY, settings.SECRET ))
    payment = client.order.create({'amount': checkout_details.total*100, 'currency':"INR", 'payment_capture':1})
    checkout_details.razor_pay_order_id = payment['id']
    checkout_details.save()
    context = {'carts':cart_qs, 'checkout':checkout_details, 'payment':payment}
    return render(request, 'shop/order-summary.html', context=context)



def success(request):
    
    chart_qs = CartItem.objects.filter(customer = request.user)
    chart_qs.delete()
    messages.success(request, 'Order placed successfully!')
    return redirect('shop:home')