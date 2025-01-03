from django.db import models
from django.conf import settings
from products.models import Product

class Review(models.Model):
    review_id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()  # Рейтинг от 1 до 5
    comment = models.TextField(blank=True, null=True)
    response = models.TextField(blank=True, null=True)  # Ответ на отзыв
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review {self.rating} for {self.product.name} by {self.user.email}"