from django.urls import path
from cart import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('add/<int:p_id>/', views.add_to_cart, name='add_cart'),
]

urlpatterns = format_suffix_patterns(urlpatterns)