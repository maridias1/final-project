from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=200, verbose_name="Title")
    description = models.TextField(verbose_name="Description")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Price ($)")
    brand = models.CharField(max_length=100, verbose_name="Brand")
    category = models.CharField(max_length=100, verbose_name="Category")
    stock = models.PositiveIntegerField(default=10, verbose_name="Stock")
    rating = models.FloatField(default=5.0, verbose_name="Rating")
    issue_date = models.DateField(auto_now_add=True, verbose_name="Release Date")
    image = models.ImageField(upload_to='products/', verbose_name="T-Shirt Image")
    def __str__(self):
        return self.title


class Review(models.Model):
    
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    name = models.CharField(max_length=100, verbose_name="Full Name")
    rating = models.PositiveIntegerField(default=5, verbose_name="Rating")
    comment = models.TextField(blank=True, verbose_name="Comment")
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.name} - {self.product.title}"