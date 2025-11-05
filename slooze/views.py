from django.shortcuts import render, redirect
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
            return render(request, 'slooze/index.html')

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


# --- SIGNUP VIEW --- #
def signup_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        if not email or not password:
            messages.error(request, "Please fill in all fields.")
            return render(request, 'slooze/index.html')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists. Please log in.")
            return redirect('login')

        User.objects.create(email=email, password=password)
        request.session['user_email'] = email
        return redirect('home')

    return render(request, 'slooze/index.html')


# --- HOME PAGE (after login) --- #
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


# --- ADD/EDIT PAGE --- #
def addedit_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
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