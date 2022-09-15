from django.urls import path
from groceries import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('ListStaff/',views.list_staff,name='ListStaff'),
    path('AddStaff',views.add_staff,name='AddStaff'),
    path('EditStaff/<int:id>',views.edit_staff,name='EditStaff'),
    path('ListProducts/',views.list_products,name='ListOfProduct'),
    path('AddProductFrozen/',views.add_product_Frozen,name='AddNewProduct1'),
    path('AddProductFresh/',views.add_product_Fresh,name='AddNewProduct2'),
    path('FreshProductDetails/<int:id>',views.fresh_product_details,name='DetailsFresh'),
    path('FrozenProductDetails/<int:id>',views.frozen_product_details,name='DetailsFrozen'),
    path('RegisterCustomer/',views.register_customer,name='Register')
    
    
]

urlpatterns = format_suffix_patterns(urlpatterns)

