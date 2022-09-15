from dataclasses import field
from wsgiref.validate import validator
from rest_framework import serializers
from groceries.models import Staff,Customers,Products

class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields= ('id','fullname','department')
        
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = ('id','fname','lname','email','categories')
         
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ('id','type','name','price')