from django.db import models

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    stock = models.PositiveIntegerField()
    sku = models.CharField(max_length=100, unique=True)
    category = models.ForeignKey('categories.Category', on_delete=models.CASCADE)
    images = models.JSONField()  # Список изображений в формате JSON
    dimensions = models.JSONField()  # Длина, ширина, высота в JSON
    weight = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name