from rest_framework import serializers

from shop.models import CartItem


class CartSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField(required=False) 
    price = serializers.SerializerMethodField()
    total_price = serializers.SerializerMethodField(read_only=True)
    customer = serializers.CharField(read_only=True)
    class Meta:
        model = CartItem
        fields= ['customer','title','quantity', 'price','total_price', 'product']


    def get_title(self,obj):
        return obj.product.title

    def get_price(self, obj):
        return obj.product.price
    
    def get_total_price(self,obj):
        return obj.quantity*obj.product.price