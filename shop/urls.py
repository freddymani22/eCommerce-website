from django.urls import path

from .views import home,detail_view,checkout

app_name = 'shop'
urlpatterns = [
    path('',home, name= 'home'),
    path('<int:id>/',detail_view, name= 'detail'),
    path('checkout/',checkout, name= 'checkout')
]