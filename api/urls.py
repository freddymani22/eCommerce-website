from django.urls import path

from .views import CartItemMixinView

urlpatterns = [
    path('', CartItemMixinView.as_view(), name='cartlist'),
    path('<int:pk>/', CartItemMixinView.as_view(), name='cartdetail'),
]