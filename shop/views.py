# Django-ს დამხმარე მეთოდები:
# render - HTML შაბლონში მონაცემების გადასაცემად და გვერდის დასაგენერირებლად
# redirect - მომხმარებლის სხვა მისამართზე (URL-ზე) გადასამისამართებლად
# get_object_or_404 - ბაზიდან ობიექტის ამოსაღებად; თუ ვერ იპოვა, ავტომატურად აბრუნებს 404 გვერდს (და სისტემა არ "იქრაშება")
from django.shortcuts import render, redirect, get_object_or_404

# მომხმარებლის სისტემაში შესვლის (login) და გამოსვლის (logout) ფუნქციები
from django.contrib.auth import login, logout

# Django-ს ჩაშენებული მზა ფორმები რეგისტრაციისთვის (UserCreationForm) და ავტორიზაციისთვის (AuthenticationForm)
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# ჩვენ მიერ models.py-ში შექმნილი მონაცემთა მოდელები
from .models import Product, Review


# ==============================================================================
# 1. მთავარი გვერდი (კატალოგი, ძებნა, ფილტრაცია კატეგორიითა და რეიტინგით)
# ==============================================================================
def product_list(request):
    # საწყისად Django ORM-ით ბაზიდან წამოვიღებთ ყველა არსებულ პროდუქტს
    products = Product.objects.all()

    # 1.1 ტექსტური ძებნა სათაურით:
    # request.GET.get('q', '') ამოწმებს URL-ში საძიებო სიტყვას (მაგ: ?q=shirt)
    query = request.GET.get('q', '').strip()
    if query:
        # title__icontains ეძებს ტექსტის დამთხვევას (i ნიშნავს case-insensitive - დიდი და პატარა ასოების გარჩევის გარეშე)
        products = products.filter(title__icontains=query)

    # 1.2 კატეგორიის ფილტრი:
    category = request.GET.get('category', '').strip()
    if category and category != 'all':
        # ფილტრავს მხოლოდ არჩეული კატეგორიის პროდუქტებს
        products = products.filter(category=category)

    # 1.3 რეიტინგის ფილტრი:
    rating = request.GET.get('rating', '').strip()
    if rating and rating != 'all':
        try:
            # რეიტინგით გაფილტვრა. rating__gte ნიშნავს Greater Than or Equal (რეიტინგი მეტია ან ტოლი მითითებულ რიცხვზე)
            products = products.filter(rating__gte=float(rating))
        except ValueError:
            # თუ პარამეტრში არასწორი მონაცემი მოხვდა, შეცდომა რომ არ ამოაგდოს, ვაიგნორებთ
            pass

    # ბაზიდან დინამიკურად ამომაქვს ყველა უნიკალური (distinct) კატეგორიის სია,
    # რათა HTML-ში ფილტრის ჩამოსაშლელ მენიუში (Dropdown) გამოჩნდეს
    categories = Product.objects.values_list('category', flat=True).distinct()
    
    # მომხმარებლის სესიიდან (Session) ვიღებთ კალათის ლექსიკონს და ვპოულობთ ნივთების რაოდენობის ჯამს
    cart = request.session.get('cart', {})
    cart_count = sum(cart.values()) # მაგალითად, ჰედერში "კალათა (3)" გამოსატანად

    # ვაბრუნებთ product_list.html-ს და ვატანთ ყველა საჭირო ცვლადს (კონტექსტს)
    return render(request, 'product_list.html', {
        'products': products,
        'categories': categories,
        'selected_category': category,
        'selected_rating': rating,
        'query': query,
        'cart_count': cart_count,
    })


# ==============================================================================
# 2. დეტალური გვერდი (ინფორმაცია მაისურზე, ტაბები და შეფასების დამატება)
# ==============================================================================
def product_detail(request, pk):
    # ეძებს პროდუქტს ID-ით. თუ ვერ იპოვა, აბრუნებს 404 გვერდს
    product = get_object_or_404(Product, pk=pk)

    # თუ მომხმარებელმა გამოაგზავნა შეფასების ფორმა (POST მოთხოვნა):
    if request.method == 'POST':
        # ფორმიდან ამოვიღებთ შევსებულ ველებს
        name = request.POST.get('name')
        rating = request.POST.get('rating', 5)
        comment = request.POST.get('comment', '')
        
        # ბაზაში ვქმნით Review მოდელის ახალ ჩანაწერს ამ კონკრეტულ პროდუქტზე
        Review.objects.create(product=product, name=name, rating=rating, comment=comment)
        
        # PRG (Post/Redirect/Get) პატერნი: მომხმარებელს გადავამისამართებთ ისევ ამ გვერდზე,
        # რათა გვერდის დარეფრეშებისას შეფასება მეორედ აღარ გაიგზავნოს
        return redirect('product_detail', pk=pk)

    # ამოგვაქვს პროდუქტზე დაწერილი ყველა შეფასება, უახლესები თავში (-created_at)
    reviews = product.reviews.all().order_by('-created_at')
    
    # კალათის მრიცხველის ამოღება ჰედერისთვის, ანუ კალათის მონაცემები ამოაქვს მომხმარებლის ბრაუზერის სესიიდან (Session) და არა ბაზიდან.
    cart = request.session.get('cart', {})
    cart_count = sum(cart.values())

    return render(request, 'product_detail.html', {
        'product': product,
        'reviews': reviews,
        'cart_count': cart_count,
    })


# ==============================================================================
# 3. კალათაში დამატება (მუშაობს ბრაუზერის სესიებზე და არა პირდაპირ ბაზაზე)
# ==============================================================================
def add_to_cart(request, pk):
    # სესიიდან ვიღებთ კალათის ლექსიკონს (Dict), თუ პირველად ამატებს - ცარიელ Dict-ს {}
    cart = request.session.get('cart', {})
    
    # ლექსიკონში გასაღები (Key) არის პროდუქტის ID (სტრინგად), ხოლო მნიშვნელობა (Value) - რაოდენობა.
    # თუ პროდუქტი უკვე იდო კალათაში, მის რაოდენობას უმატებს 1-ს, თუ არა — წერს 1-ს
    cart[str(pk)] = cart.get(str(pk), 0) + 1
    
    # განახლებულ კალათას ისევ ვინახავთ მომხმარებლის სესიაში
    request.session['cart'] = cart
    
    # HTTP_REFERER მომხმარებელს აბრუნებს ზუსტად იმ გვერდზე, სადაც ღილაკს დააჭირა
    return redirect(request.META.get('HTTP_REFERER', 'product_list'))


# ==============================================================================
# 4. კალათის გვერდი (დამატებული ნივთები, რაოდენობები და ჯამური თანხა)
# ==============================================================================
def cart_view(request):
    cart = request.session.get('cart', {})
    items = []
    total_price = 0

    # ციკლით გადავუყვებით კალათის ყველა ელემენტს (pk = ID, quantity = რაოდენობა)
    for pk, quantity in cart.items():
        # ბაზიდან ვპოულობთ შესაბამის პროდუქტს
        product = Product.objects.filter(pk=pk).first()
        if product:
            item_total = product.price * quantity # კონკრეტული მაისურის ჯამური ფასი
            total_price += item_total             # მთლიანი კალათის ღირებულება
            
            # სიაში ვამატებთ პროდუქტის სრულ მონაცემებს HTML-ში გამოსატანად
            items.append({
                'product': product,
                'quantity': quantity,
                'item_total': item_total,
                'reviews_count': product.reviews.count(),
            })

    cart_count = sum(cart.values())

    # ვაბრუნებთ cart.html-ს გამოთვლილი ჯამური თანხითა და ნივთებით
    return render(request, 'cart.html', {
        'items': items,
        'total_price': total_price,
        'cart_count': cart_count,
    })


# ==============================================================================
# 4.1 კალათაში რაოდენობის მართვა (+, -, ან სრული წაშლა)
# ==============================================================================
def update_cart(request, pk, action):
    cart = request.session.get('cart', {})
    str_pk = str(pk)
    
    # თუ ეს პროდუქტი მართლაც დევს კალათაში:
    if str_pk in cart:
        if action == 'plus':
            cart[str_pk] += 1 # რაოდენობის გაზრდა
        elif action == 'minus':
            cart[str_pk] -= 1 # რაოდენობის შემცირება
            # თუ რაოდენობა ჩამოვიდა 0-ზე ან ნაკლებზე, მთლიანად ვშლით კალათიდან ნივთს.
            if cart[str_pk] <= 0:
                del cart[str_pk]
        elif action == 'delete':
            # პირდაპირ ვშლით ნივთს კალათიდან
            del cart[str_pk]
            
    # ცვლილებების შენახვა სესიაში
    request.session['cart'] = cart
    
    # ვაბრუნებთ კალათის გვერდზე განახლებული მონაცემებით
    return redirect('cart')


# ==============================================================================
# 5. მომხმარებლის ავთენტიფიკაციის სისტემა (Auth)
# ==============================================================================

# 5.1 ახალი მომხმარებლის რეგისტრაცია
def user_register(request):
    if request.method == 'POST':
        # ივსება Django-ს ჩაშენებული რეგისტრაციის ფორმა მომხმარებლის გამოგზავნილი მონაცემებით
        form = UserCreationForm(request.POST)
        if form.is_valid(): # თუ პაროლი და იუზერნეიმი ვალიდურია:
            user = form.save()   # მომხმარებელი ინახება auth_user ბაზაში
            login(request, user) # მომხმარებლის სისტემაში შესვლა და მისი ავტორიზებული სესიის შექმნა
            return redirect('product_list')
    else:
        # თუ ჩვეულებრივი GET მოთხოვნაა, ვხსნით ცარიელ ფორმას
        form = UserCreationForm()
        
    return render(request, 'register.html', {'form': form})


# 5.2 სისტემაში შესვლა (ავტორიზაცია / Login)
def user_login(request):
    if request.method == 'POST':
        # AuthenticationForm ამოწმებს, ემთხვევა თუ არა იუზერნეიმი და პაროლი ბაზაში არსებულს
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user() # ვიღებთ დადასტურებულ იუზერს
            login(request, user)   # ვქმნით მომხმარებლის ავტორიზებულ სესიას
            return redirect('product_list')
    else:
        form = AuthenticationForm()
        
    return render(request, 'login.html', {'form': form})


# 5.3 სისტემიდან გამოსვლა (Logout)
def user_logout(request):
    logout(request) # ვშლით მიმდინარე ავტორიზაციის სესიას
    return redirect('product_list')