# ეს ფაილი ავტომატურად დააგენერირა Django-მ 'python manage.py makemigrations' ბრძანების გაშვებისას
# თარიღი: 2026 წლის 2 ნოემბერი

# Django-ს მიგრაციებისა და მოდელების მოდულების შემოტანა
from django.db import migrations, models


# Migration კლასი აღწერს, რა ცვლილებები უნდა შევიდეს მონაცემთა ბაზაში (SQLite-ში)
class Migration(migrations.Migration):

    # initial = True ნიშნავს, რომ ეს არის shop აპლიკაციის პირველი (საწყისი) მიგრაცია
    initial = True

    # dependencies არის სია, თუ რომელ წინა მიგრაციებზეა დამოკიდებული ეს ფაილი.
    # რადგან საწყისია, სია ცარიელია []
    dependencies = [
    ]

    # operations განსაზღვრავს კონკრეტულ ოპერაციებს, რასაც Django შეასრულებს ბაზაში
    operations = [
        # migrations.CreateModel ქმნის ახალ ცხრილს მონაცემთა ბაზაში სახელწოდებით 'Product'
        migrations.CreateModel(
            name='Product',
            # fields-ში ჩამოწერილია ბაზის ცხრილის სვეტები (ველები)
            fields=[
                # 'id' ველი ავტომატურად იქმნება Django-ს მიერ, როგორც უნიკალური პირველადი გასაღები (Primary Key, Auto Increment)
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                
                # Product მოდელის ველები, რომლებიც models.py-ში გვქონდა გაწერილი:
                ('title', models.CharField(max_length=200, verbose_name='დასახელება')),
                ('description', models.TextField(verbose_name='აღწერა')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='ფასი ($)')),
                ('brand', models.CharField(max_length=100, verbose_name='ბრენდი')),
                ('category', models.CharField(max_length=100, verbose_name='კატეგორია')),
                ('stock', models.PositiveIntegerField(default=10, verbose_name='მარაგი (Stock)')),
                ('rating', models.FloatField(default=5.0, verbose_name='რეიტინგი')),
                ('issue_date', models.DateField(auto_now_add=True, verbose_name='გამოშვების თარიღი')),
                ('image', models.ImageField(upload_to='products/', verbose_name='მაისურის ფოტო')),
            ],
        ),
    ]