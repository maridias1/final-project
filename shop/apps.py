# Django-ს აპლიკაციის კონფიგურაციის საბაზისო კლასის შემოტანა
from django.apps import AppConfig


# ShopConfig კლასი განსაზღვრავს 'shop' აპლიკაციის კონფიგურაციასა და მეტამონაცემებს
class ShopConfig(AppConfig):
    # default_auto_field მიუთითებს ბაზაში პირველადი გასაღების (ID / Primary Key) ტიპს
    default_auto_field = 'django.db.models.BigAutoField'
    
    # აპლიკაციის უნიკალური სახელი პროექტის შიგნით (ფოლდერის სახელი)
    name = 'shop'