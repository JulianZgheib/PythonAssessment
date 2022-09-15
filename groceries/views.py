from groceries.serializers import StaffSerializer,CustomerSerializer,ProductSerializer
from groceries.models import Staff,Products
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.validators import UniqueValidator
# Create your views here.

#INTERNAL STAFF APIs 
@api_view(['GET'])
def list_staff(request,format=None):
    if request.method == 'GET':
        staff = Staff.objects.all()
        serializer = StaffSerializer(staff,many=True)
        return JsonResponse({'List Of Staff':serializer.data})
    
@api_view(['POST'])
def add_staff(request,format=None):       
    if request.method =='POST':
            serializer= StaffSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(status=status)

@api_view(['GET','PUT','DELETE'])
def edit_staff(request,id):
    try:
        staff = Staff.objects.get(pk=id)
    except Staff.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = StaffSerializer(staff)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer= StaffSerializer(staff,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method =='DELETE':
        staff.delete()
        print("Deleted")
        return Response(status=status.HTTP_204_NO_CONTENT)

# Customer Registration
@api_view(['POST'])
def new_customer(request,format=None):
    if request.method =='POST':
         serializer= CustomerSerializer(data = request.data)
         if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(status=status)

############### ALL Product ##############
@api_view(['GET'])
def list_products(request,format=None):
    product = Products.objects.all()
    if request.method =='GET':
        serializer = ProductSerializer(product,many=True)
        return JsonResponse({'List Of Products':serializer.data})

########### Fresh Product APIs #############
@api_view(['POST'])
def add_product_Fresh(request,format=None):
    type = request.data['type']       
    if request.method =='POST' and type == 'fresh food' :
            serializer= ProductSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(status=status)

@api_view(['GET','PUT','DELETE'])
def fresh_product_details(request,id):
    try:
        product = Products.objects.get(pk=id)
    except Staff.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    
    elif request.method == 'PUT' and request.data['type'] == 'fresh food':
        serializer= ProductSerializer(product,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method =='DELETE' and request.data['type'] == 'fresh food ':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
####### Frozen Product APIs ############### 
@api_view(['POST'])
def add_product_Frozen(request,format=None):
    type = request.data['type']       
    if request.method =='POST' and type == 'frozen food' :
            serializer= ProductSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(status=status)

@api_view(['GET','PUT','DELETE'])
def frozen_product_details(request,id):
    try:
        product = Products.objects.get(pk=id)
    except Staff.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET' :
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    
    elif request.method == 'PUT' and request.data['type'] == 'frozen food':
        serializer= ProductSerializer(product,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method =='DELETE' and request.data['type'] == 'frozen food':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
#########################################################
##### Customer Sign in #########
@api_view(['POST'])
def register_customer(request):
    pass