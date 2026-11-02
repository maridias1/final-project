from django.db import models

# 1. პროდუქტის (მაისურის) მოდელი
class Product(models.Model):
    title = models.CharField(max_length=200, verbose_name="დასახელება")
    description = models.TextField(verbose_name="აღწერა")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="ფასი ($)")
    brand = models.CharField(max_length=100, verbose_name="ბრენდი")
    category = models.CharField(max_length=100, verbose_name="კატეგორია")
    stock = models.PositiveIntegerField(default=10, verbose_name="მარაგი (Stock)")
    rating = models.FloatField(default=5.0, verbose_name="რეიტინგი")
    issue_date = models.DateField(auto_now_add=True, verbose_name="გამოშვების თარიღი")
    image = models.ImageField(upload_to='products/', verbose_name="მაისურის ფოტო")

    def __str__(self):
        return self.title


# 2. შეფასებების (Review) მოდელი
class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    name = models.CharField(max_length=100, verbose_name="შემფასებლის სახელი და გვარი")
    rating = models.PositiveIntegerField(default=5, verbose_name="რეიტინგი")
    comment = models.TextField(blank=True, verbose_name="კომენტარი")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.product.title}"