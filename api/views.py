from rest_framework import generics, mixins
from rest_framework.response import Response

from rest_framework.permissions import IsAuthenticated

from shop.models import CartItem,Product
from api.serializers import CartSerializer

class CartItemMixinView(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView
):
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'pk'

    def get_queryset(self):
        return CartItem.objects.filter(customer=self.request.user)

    def get(self, request, pk=None, *args, **kwargs):
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)
    
    def post(self, request, pk=None, *args, **kwargs):
        if pk is not None:
            return self.update(request, *args, **kwargs)
        customer = self.request.user
        product = self.request.data.get('product')
        quantity = self.request.data.get('quantity')
        if quantity=='' or quantity is None:
            quantity = 1
        else:
            quantity = int(quantity)


        product_obj = Product.objects.get(id=product)

        try:
            cartitem_obj = CartItem.objects.get(customer=customer, product=product_obj)
            cartitem_obj.quantity +=quantity
            cartitem_obj.save()
            serializer = self.get_serializer(cartitem_obj)
            return Response(serializer.data)
        except CartItem.DoesNotExist:
            return self.create(request, customer = self.request.user, *args, **kwargs)
     

    def perform_create(self, serializer):
        customer = self.request.user
        product = serializer.validated_data.get('product')
        quantity = serializer.validated_data.get('quantity')

        if quantity is None:
            quantity = 1
        else:
            quantity = int(quantity)
            
        product_obj = Product.objects.get(title=product)
        serializer.save(customer=customer, product=product_obj, quantity=quantity)
      


        
        

class DeleteCartItemApiView(generics.RetrieveDestroyAPIView):
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'pk'


    def get_queryset(self):
        return CartItem.objects.filter(customer=self.request.user)
    




    