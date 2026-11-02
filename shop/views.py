from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Product, Review

# 1. მთავარი გვერდი
def product_list(request):
    products = Product.objects.all()

    query = request.GET.get('q', '').strip()
    if query:
        products = products.filter(title__icontains=query)

    category = request.GET.get('category', '').strip()
    if category and category != 'all':
        products = products.filter(category=category)

    rating = request.GET.get('rating', '').strip()
    if rating and rating != 'all':
        try:
            products = products.filter(rating__gte=float(rating))
        except ValueError:
            pass

    categories = Product.objects.values_list('category', flat=True).distinct()
    
    # კალათაში არსებული ნივთების რაოდენობა ჰედერის მრიცხველისთვის
    cart = request.session.get('cart', {})
    cart_count = sum(cart.values())

    return render(request, 'product_list.html', {
        'products': products,
        'categories': categories,
        'selected_category': category,
        'selected_rating': rating,
        'query': query,
        'cart_count': cart_count,
    })

# 2. დეტალური გვერდი (Tabs: Details და Review + შეფასების დამატება)
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        name = request.POST.get('name')
        rating = request.POST.get('rating', 5)
        comment = request.POST.get('comment', '')
        Review.objects.create(product=product, name=name, rating=rating, comment=comment)
        return redirect('product_detail', pk=pk)

    reviews = product.reviews.all().order_by('-created_at')
    cart = request.session.get('cart', {})
    cart_count = sum(cart.values())

    return render(request, 'product_detail.html', {
        'product': product,
        'reviews': reviews,
        'cart_count': cart_count,
    })

# 3. კალათაში დამატება
def add_to_cart(request, pk):
    cart = request.session.get('cart', {})
    cart[str(pk)] = cart.get(str(pk), 0) + 1
    request.session['cart'] = cart
    return redirect(request.META.get('HTTP_REFERER', 'product_list'))

# 4. კალათის გვერდი (+, -, წაშლა, ჯამური ფასი)
def cart_view(request):
    cart = request.session.get('cart', {})
    items = []
    total_price = 0

    for pk, quantity in cart.items():
        product = Product.objects.filter(pk=pk).first()
        if product:
            item_total = product.price * quantity
            total_price += item_total
            items.append({
                'product': product,
                'quantity': quantity,
                'item_total': item_total,
                'reviews_count': product.reviews.count(),
            })

    cart_count = sum(cart.values())

    return render(request, 'cart.html', {
        'items': items,
        'total_price': total_price,
        'cart_count': cart_count,
    })

# კალათაში რაოდენობის შეცვლა (+ ან -)
def update_cart(request, pk, action):
    cart = request.session.get('cart', {})
    str_pk = str(pk)
    if str_pk in cart:
        if action == 'plus':
            cart[str_pk] += 1
        elif action == 'minus':
            cart[str_pk] -= 1
            if cart[str_pk] <= 0:
                del cart[str_pk]
        elif action == 'delete':
            del cart[str_pk]
    request.session['cart'] = cart
    return redirect('cart')

# 5. Auth (რეგისტრაცია, ლოგინი, გასვლა)
def user_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('product_list')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('product_list')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('product_list')