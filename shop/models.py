# Django-ს მონაცემთა ბაზასთან სამუშაო მთავარი მოდულის შემოტანა
from django.db import models


# ==============================================================================
# 1. პროდუქტის (მაისურის) მოდელი - ბაზაში ქმნის პროდუქტების ცხრილს
# ==============================================================================
class Product(models.Model):
    # CharField გამოიყენება მოკლე ტექსტისთვის; max_length ზღუდავს სიმბოლოების რაოდენობას
    title = models.CharField(max_length=200, verbose_name="დასახელება")
    
    # TextField გამოიყენება დიდი მოცულობის ტექსტისთვის (პროდუქტის სრული აღწერა)
    description = models.TextField(verbose_name="აღწერა")
    
    # DecimalField გამოიყენება ფასისთვის (10 ციფრი მთლიანად, 2 ათწილადი მძიმის შემდეგ).
    # Float-ის ნაცვლად Decimal-ს ვიყენებთ, რომ ფინანსური დამრგვალების ცდომილება არ მოხდეს
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="ფასი ($)")
    
    # ბრენდის და კატეგორიის სახელწოდებები მოკლე ტექსტის სახით
    brand = models.CharField(max_length=100, verbose_name="ბრენდი")
    category = models.CharField(max_length=100, verbose_name="კატეგორია")
    
    # PositiveIntegerField ინახავს მხოლოდ დადებით მთელ რიცხვებს; default=10 არის საწყისი მარაგი
    stock = models.PositiveIntegerField(default=10, verbose_name="მარაგი (Stock)")
    
    # FloatField გამოიყენება ათწილადი რიცხვებისთვის (პროდუქტის საშუალო შეფასება/ვარსკვლავები)
    rating = models.FloatField(default=5.0, verbose_name="რეიტინგი")
    
    # auto_now_add=True ავტომატურად იწერს პროდუქტის ბაზაში დამატების მიმდინარე თარიღს
    issue_date = models.DateField(auto_now_add=True, verbose_name="გამოშვების თარიღი")
    
    # upload_to='products/' მიუთითებს, რომ ატვირთული ფოტო შეინახოს media/products/ საქაღალდეში
    image = models.ImageField(upload_to='products/', verbose_name="მაისურის ფოტო")

    # __str__ მეთოდი განსაზღვრავს, რა ტექსტით გამოჩნდეს ეს ობიექტი Django-ს ადმინ-პანელში (გამოაქვს სათაური)
    def __str__(self):
        return self.title


# ==============================================================================
# 2. შეფასებების (Review) მოდელი - ბაზაში ქმნის შეფასებების ცხრილს
# ==============================================================================
class Review(models.Model):
    # ForeignKey ქმნის "One-to-Many" (ერთი ბევრთან) კავშირს პროდუქტთან (ერთ მაისურს შეიძლება ჰქონდეს ბევრი შეფასება).
    # on_delete=models.CASCADE ნიშნავს: თუ პროდუქტი წაიშლება ბაზიდან, მასზე დაწერილი შეფასებებიც ავტომატურად წაიშალოს.
    # related_name='reviews' გვაძლევს საშუალებას, პროდუქტის მხრიდან მარტივად წამოვიღოთ შეფასებები: product.reviews.all()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    
    # შემფასებლის სახელი და გვარი
    name = models.CharField(max_length=100, verbose_name="შემფასებლის სახელი და გვარი")
    
    # მომხმარებლის მიერ დაწერილი ქულა (1-დან 5-მდე)
    rating = models.PositiveIntegerField(default=5, verbose_name="რეიტინგი")
    
    # blank=True ნიშნავს, რომ კომენტარის ველის ცარიელად დატოვება ნებადართულია (სავალდებულო არაა)
    comment = models.TextField(blank=True, verbose_name="კომენტარი")
    
    # auto_now_add=True ავტომატურად აფიქსირებს შეფასების დაწერის ზუსტ დროსა და წამს
    created_at = models.DateTimeField(auto_now_add=True)

    # ადმინ-პანელში გამოიტანს ფორმატს: "შემფასებლის სახელი - პროდუქტის სახელი"
    def __str__(self):
        return f"{self.name} - {self.product.title}"