from rest_framework import serializers
from .models import Product
from categories.models import Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'parent', 'created_at']

class ProductSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())

    class Meta:
        model = Product
        fields = [
            'product_id', 'name', 'description', 'price', 'discount', 'stock',
            'sku', 'category', 'images', 'dimensions', 'weight', 'created_at'
        ]