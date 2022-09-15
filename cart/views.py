from .models import Cart, Cart_items
from rest_framework.decorators import api_view
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from groceries.models import Products
from rest_framework.exceptions import NotFound, ParseError


@api_view(['GET','POST'])
def add_to_cart(request, p_id):
    user = {
            'username':request.GET["username"],
            'password':request.GET["password"]
            }
   # print(request.GET["username"], request.GET["password"])
   # print(user)
    try:
        product = Products.objects.get(pk=p_id)
        quantity = int(float(request.GET["quantity"]))
        if quantity < 1:
            raise ParseError("The number of items to be added must be at least 1")
        elif product.inventory_count == 0 or product.inventory_count < quantity < 1:
            raise ParseError("The product {0} does not have sufficient inventory".format(p_id))

    except ObjectDoesNotExist:
        raise NotFound("Product {0} is not found, please try another product".format(p_id))

    try:
        cart = Cart.objects.get(customer=user)
    except ObjectDoesNotExist:
        cart = Cart.objects.create(customer=user)

    try:
        cart_item = Cart_items.objects.get(cart=cart, product=product)
        cart_item.quantity += quantity
        cart_item.save()
    except ObjectDoesNotExist:
        cart_item = Cart_items.objects.create(cart=cart, product=product, quantity=quantity)

    cart.total += quantity * float(product.price)
    cart.save()
    cur_cart = {}
    for item in Cart_items.objects.filter(cart=cart):
        cur_cart[item.product.title] = item.quantity

    return JsonResponse({'Status': "Product {0} is added successfully to the shopping cart".format(p_id), "Cart":cur_cart})

@api_view(['GET'])
def show_cart(request):
    pass

@api_view(['GET','PUT','DELETE'])
def edit_cart(request):
    pass