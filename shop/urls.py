from django.urls import path

from .views import home,detail_view,checkout, order_summary,success

app_name = 'shop'
urlpatterns = [
    path('',home, name= 'home'),
    path('<int:id>/',detail_view, name= 'detail'),
    path('checkout/',checkout, name= 'checkout'),
    path('summary/',order_summary, name= 'summary'),
    path('success/',success, name= 'suceess')
]