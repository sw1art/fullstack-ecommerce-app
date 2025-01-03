from django.db import models
from django.conf import settings
from products.models import Product

class Cart(models.Model):
    cart_id = models.AutoField(primary_key=True)  # Используем cart_id вместо id
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Cart {self.cart_id} for User {self.user_id}"

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    added_at = models.DateTimeField(auto_now_add=True)
    price_at_addition = models.DecimalField(max_digits=10, decimal_places=2)
    discount_at_addition = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    status = models.CharField(max_length=50, default="active")

    def __str__(self):
        return f"Item {self.product.name} in Cart {self.cart.cart_id}"
