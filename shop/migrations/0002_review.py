# ეს ფაილი ავტომატურად დააგენერირა Django-მ მას შემდეგ, რაც models.py-ში დავამატეთ Review მოდელი
# თარიღი: 2026 წლის 2 ნოემბერი

# ForeignKey-ს წაშლის წესისთვის (CASCADE) საჭირო მოდული
import django.db.models.deletion

# Django-ს მიგრაციებისა და მოდელების მოდულების შემოტანა
from django.db import migrations, models


class Migration(migrations.Migration):

    # dependencies: ეს მიგრაცია პირდაპირ დამოკიდებულია წინა მიგრაციაზე ('0001_initial'),
    # რადგან Review მოდელი ვერ შეიქმნება მანამ, სანამ Product მოდელი არ იარსებებს ბაზაში!
    dependencies = [
        ('shop', '0001_initial'),
    ]

    # operations: ოპერაციები, რასაც ეს მიგრაცია ბაზაში ასრულებს
    operations = [
        # migrations.CreateModel ბაზაში ქმნის ახალ ცხრილს სახელწოდებით 'Review' (შეფასებები)
        migrations.CreateModel(
            name='Review',
            fields=[
                # უნიკალური ID (Primary Key) შეფასებისთვის
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                
                # შემფასებლის სახელი და გვარი
                ('name', models.CharField(max_length=100, verbose_name='შემფასებლის სახელი და გვარი')),
                
                # რეიტინგი (ვარსკვლავები 1-დან 5-მდე)
                ('rating', models.PositiveIntegerField(default=5, verbose_name='რეიტინგი')),
                
                # კომენტარი (სურვილისამებრ, blank=True)
                ('comment', models.TextField(blank=True, verbose_name='კომენტარი')),
                
                # შეფასების დაწერის დრო
                ('created_at', models.DateTimeField(auto_now_add=True)),
                
                # საგარეო გასაღები (ForeignKey):
                # აკავშირებს ამ შეფასებას 'shop.product' მოდელთან (One-to-Many კავშირი).
                # on_delete=CASCADE ნიშნავს: თუ პროდუქტი წაიშლება, მისი შეფასებებიც წაიშლება ბაზიდან.
                # related_name='reviews' გვაძლევს პროდუქტის მხრიდან წვდომას: product.reviews.all()
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='shop.product')),
            ],
        ),
    ]