from django.db import migrations, models
class Migration(migrations.Migration):
    initial = True
    dependencies = [
    ]
    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('description', models.TextField(verbose_name='Description')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Price ($)')),
                ('brand', models.CharField(max_length=100, verbose_name='Brand')),
                ('category', models.CharField(max_length=100, verbose_name='Category')),
                ('stock', models.PositiveIntegerField(default=10, verbose_name='Stock')),
                ('rating', models.FloatField(default=5.0, verbose_name='Rating')),
                ('issue_date', models.DateField(auto_now_add=True, verbose_name='Release Date')),
                ('image', models.ImageField(upload_to='products/', verbose_name='T-Shirt Image')),
            ],
        ),
    ]