from .models import Category
from django.shortcuts import render, redirect, get_object_or_404
from django import forms
from .models import Picture
from .forms import PictureForm
from django.shortcuts import get_object_or_404, redirect



# def upload_picture(request):
    
#     return render(request, "gallery/upload_picture.html", {"form": form})


# class PictureForm(forms.ModelForm):
#     class Meta:
#         model = Picture
#         fields = ["title", "image"]  # Вказуємо поля, які потрібно відобразити у формі


def index(request):
    categories = Category.objects.all()
    return render(
        request, "gallery/index.html", {"categories": categories}
    )


def category_pictures(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    pictures = category.pictures.all()
    if request.method == "POST":
        form = PictureForm(request.POST, request.FILES)
        if form.is_valid():
            Picture.objects.create(image=form.cleaned_data["image"],title=form.cleaned_data["title"], category=category)
            form = PictureForm()
    else:
        form = PictureForm()
    return render(
        request,
        "gallery/category_pictures.html",
        {"category": category, "pictures": pictures, "form": form},
    )


def index(request):
    categories = Category.objects.all()
    return render(
        request, "gallery/index.html", {"categories": categories}
    )


# def picture(request):
#     nature_category = get_object_or_404(
#         Category, name="Природа"
#     )  # Отримуємо категорію природи
#     return render(
#         request, "gallery/picture.html", {"category": nature_category}
#     )


# def category_pictures(request, category_id):
#     category = get_object_or_404(Category, id=category_id)
#     pictures = category.pictures.all()
#     return render(
#         request,
#         "gallery/category_pictures.html",
#         {"category": category, "pictures": pictures},
#     )
def delete_picture(request, picture_id):
    # Отримуємо картинку за ID або повертаємо помилку 404, якщо такої немає
    picture = get_object_or_404(Picture, id=picture_id)

    # Перевіряємо, чи це POST-запит для підтвердження видалення
    if request.method == 'POST':
        picture.delete()  # Видаляємо картинку з бази даних
        return redirect('{{ picture.image.url }}')  # Переадресовуємо користувача після видалення

    # Повертаємо іншу відповідь, якщо запит не є POST
    return redirect('{{ picture.image.url }}')