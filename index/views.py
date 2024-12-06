from django.shortcuts import render
from .models import Category, Product, Cart


# Create your views here.
# Главная страница
def home_page(request):
    # Достаем данные из БД
    products = Product.objects.all()
    categories = Category.objects.all()
    # Передаем данные на Frontend
    context = {'products': products, 'categories': categories}

    return render(request, 'home.html', context)


# Вывод товаров по выбранной категории
def category_page(request, pk):
    # Достаем выбранную категорию
    category = Category.objects.get(id=pk)
    # Фильтруем товары по категории
    products = Product.objects.filter(product_category=category)
    print(products)
    # Передаем данные на Frontend
    context = {'category': category, 'products': products}

    return render(request, 'category.html', context)


# Вывод определенного товара
def product_page(request, pk):
    # Вывод выбранного товара
    product = Product.objects.get(id=pk)
    # Передаем данные на Frontend
    context = {'product': product}

    return render(request, 'product.html', context)











