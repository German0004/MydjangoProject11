from django.shortcuts import render, get_object_or_404
from .models import Category


def index(request):
    categories = Category.objects.all()
    return render(request, "gallery/index.html", {"categories": categories})


def category_pictures(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    pictures = category.pictures.all()
    return render(
        request,
        "gallery/category_pictures.html",
        {"category": category, "pictures": pictures},
    )


# gallery/views.py
from django.shortcuts import render, get_object_or_404
from .models import Category


def index(request):
    categories = Category.objects.all()
    return render(request, "gallery/index.html", {"categories": categories})


def picture(request):
    nature_category = get_object_or_404(
        Category, name="Природа"
    )  # Отримуємо категорію природи
    return render(request, "gallery/picture.html", {"category": nature_category})


def category_pictures(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    pictures = category.pictures.all()
    return render(
        request,
        "gallery/category_pictures.html",
        {"category": category, "pictures": pictures},
    )
