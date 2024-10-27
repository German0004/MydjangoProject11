from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path(
        "category/<int:category_id>/", views.category_pictures, name="category_pictures"
    ),
    path("gallery/", views.picture, name="picture"),  # Нова URL для сторінки Picture
    path(
        "category/<int:category_id>/", views.category_pictures, name="category_pictures"
    ),
]
