from rest_framework import serializers
from .models import Order, OrderItem, Transaction

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['order_item_id', 'order', 'product', 'quantity', 'price', 'discount', 'subtotal']

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['transaction_id', 'order', 'payment_method', 'payment_status', 'transaction_date', 'payment_reference', 'amount']

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    transactions = TransactionSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ['order_id', 'buyer', 'shipping_address', 'total_amount', 'delivery_fee', 'status', 'tracking_number', 'delivery_service', 'payment_status', 'created_at', 'items', 'transactions']
