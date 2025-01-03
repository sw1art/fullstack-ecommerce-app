from django.urls import path
from .views import CartListCreateView, CartRetrieveUpdateDestroyView, CartItemCreateView, CartItemRetrieveUpdateDestroyView

urlpatterns = [
    path('', CartListCreateView.as_view(), name='cart-list-create'),
    path('<int:pk>/', CartRetrieveUpdateDestroyView.as_view(), name='cart-detail'),
    path('items/', CartItemCreateView.as_view(), name='cart-item-create'),
    path('items/<int:pk>/', CartItemRetrieveUpdateDestroyView.as_view(), name='cart-item-detail'),
]
