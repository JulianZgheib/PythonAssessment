from rest_framework import serializers
from groceries.models import Staff,Customers,Products

class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields= ('id','fullname','department')
        
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = ('id','fname','lname','email','password','categories')
         
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ('id','type','name','price')

