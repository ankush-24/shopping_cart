from rest_framework import serializers

from user import models


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = ('name','price','description')

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Cart
        fields = ('product','quantity','subtotal','user')        

# class BelongingSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.Belonging
#         fields = ('id', 'name')

# class BorrowedSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.Borrowed
#         fields = ('id', 'what', 'to_who', 'when', 'returned')