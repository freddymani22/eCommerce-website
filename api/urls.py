from django.urls import path

from .views import CartItemMixinView, DeleteCartItemApiView

urlpatterns = [
    path('', CartItemMixinView.as_view(), name='cartlist'),
    path('<int:pk>/', DeleteCartItemApiView.as_view(), name='cartdelete'),
]