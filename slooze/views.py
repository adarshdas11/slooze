from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import User, Product


# --- LOGIN VIEW --- #
def login_view(request):
    if 'user_email' in request.session:
        return redirect('home')

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        if not email or not password:
            messages.error(request, "Please enter both email and password.")
            return redirect('login')

        try:
            user = User.objects.get(email=email)
            if user.password == password:
                request.session['user_email'] = user.email
                return redirect('home')
            else:
                messages.error(request, "Incorrect password.")
        except User.DoesNotExist:
            messages.error(request, "No account found. Please sign up first.")
            return redirect('signup')

    return render(request, 'slooze/index.html')


# --- SIGNUP VIEW (New Page) --- #
def signup_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        if not email or not password:
            messages.error(request, "Please enter email and password.")
            return redirect('signup')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists. Please login.")
            return redirect('login')

        User.objects.create(email=email, password=password)
        messages.success(request, "Account created successfully. Please login now.")
        return redirect('login')

    return render(request, 'slooze/signup.html')


# --- HOME PAGE (AFTER LOGIN) --- #
def home_view(request):
    if 'user_email' not in request.session:
        return redirect('login')
    return render(request, 'slooze/home.html')


# --- LOGOUT --- #
def logout_view(request):
    request.session.flush()
    return redirect('login')


# --- DASHBOARD PAGE --- #
def dashboard_view(request):
    if 'user_email' not in request.session:
        return redirect('login')

    recent_sales = ['Adarsh', 'John Doe', 'Emily', 'David', 'Sophia']
    return render(request, 'slooze/dashboard.html', {'recent_sales': recent_sales})


# --- PRODUCTS PAGE --- #
def products_view(request):
    products = Product.objects.all()
    return render(request, 'slooze/products.html', {'products': products})


# --- ADD / EDIT PRODUCT PAGE --- #
def addedit_view(request):
    if request.method == "POST":
        name = request.POST.get("product_name")
        category = request.POST.get("category")
        description = request.POST.get("description")
        price = request.POST.get("price")
        stock = request.POST.get("stock")

        Product.objects.create(
            name=name,
            category=category,
            description=description,
            price=price,
            stock=stock,
        )
        return redirect('products')

    return render(request, 'slooze/addedit.html')


# --- EDIT PRODUCT VIEW (Updated) --- #
def edit_product_view(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == "POST":
        product.name = request.POST.get("name", "").strip()
        product.category = request.POST.get("category", "").strip()
        product.price = request.POST.get("price", 0)
        product.stock = request.POST.get("stock", 0)

        if product.name == "":
            return redirect("products")

        product.save()
        return redirect("products")

    return redirect("products")


# --- DELETE PRODUCT VIEW --- #
def delete_product_view(request, id):
    product = Product.objects.get(id=id)
    product.delete()
    return redirect('products')
