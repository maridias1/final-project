# path ფუნქცია გამოიყენება URL მისამართების (მარშრუტების) განსასაზღვრად
from django.urls import path

# . ნიშნავს იმავე საქაღალდეს, საიდანაც შემოგვაქვს views.py (ხედების ფაილი)
from . import views

# urlpatterns სიაში გაწერილია საიტის ყველა შესაძლო ბმული (მარშრუტი)
urlpatterns = [
    # 1. მთავარი გვერდი (ცარიელი სტრინგი '' ნიშნავს საიტის მთავარ დომენს / ფესვს).
    # მომხმარებლის შესვლისას ეშვება views.py-ში არსებული product_list ფუნქცია.
    # name='product_list' გამოიყენება HTML შაბლონებში ბმულის მარტივად გამოსაძახებლად: {% url 'product_list' %}
    path('', views.product_list, name='product_list'),

    # 2. პროდუქტის დეტალური გვერდი.
    # <int:pk> არის დინამიკური პარამეტრი (მთელი რიცხვი - პროდუქტის ID), მაგალითად: /product/3/
    path('product/<int:pk>/', views.product_detail, name='product_detail'),

    # 3. კალათის მთავარი გვერდი, სადაც მომხმარებელი ხედავს დამატებულ ნივთებსა და ჯამურ თანხას
    path('cart/', views.cart_view, name='cart'),

    # 4. კალათაში კონკრეტული პროდუქტის დამატების მისამართი (იღებს პროდუქტის ID-ს: <int:pk>)
    path('cart/add/<int:pk>/', views.add_to_cart, name='add_to_cart'),

    # 5. კალათაში რაოდენობის შეცვლის ან წაშლის მისამართი.
    # იღებს 2 დინამიკურ მნიშვნელობას:
    # <int:pk> - პროდუქტის ID
    # <str:action> - მოქმედების სახელი (ტექსტურად: 'plus', 'minus', ან 'delete')
    path('cart/update/<int:pk>/<str:action>/', views.update_cart, name='update_cart'),

    # 6. მომხმარებლის რეგისტრაციის გვერდი
    path('register/', views.user_register, name='register'),

    # 7. სისტემაში შესვლის (ავტორიზაციის / Login-ის) გვერდი
    path('login/', views.user_login, name='login'),

    # 8. სისტემიდან გამოსვლის (Logout-ის) მისამართი
    path('logout/', views.user_logout, name='logout'),
]