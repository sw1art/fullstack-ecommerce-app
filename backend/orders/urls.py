from django.urls import path
from .views import (
    OrderListCreateView, OrderRetrieveUpdateDestroyView,
    OrderItemListCreateView, OrderItemRetrieveUpdateDestroyView,
    TransactionListCreateView, TransactionRetrieveUpdateDestroyView
)

urlpatterns = [
    path('', OrderListCreateView.as_view(), name='order-list-create'),
    path('<int:pk>/', OrderRetrieveUpdateDestroyView.as_view(), name='order-detail'),
    path('items/', OrderItemListCreateView.as_view(), name='order-item-list-create'),
    path('items/<int:pk>/', OrderItemRetrieveUpdateDestroyView.as_view(), name='order-item-detail'),
    path('transactions/', TransactionListCreateView.as_view(), name='transaction-list-create'),
    path('transactions/<int:pk>/', TransactionRetrieveUpdateDestroyView.as_view(), name='transaction-detail'),
]
