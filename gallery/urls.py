from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    # path(
    #     "upload/", views.upload_picture, name="upload_picture"
    # ),  # URL для завантаження картинки
    path(
        "category/<int:category_id>/", views.category_pictures, name="category_pictures"
    ),
    # path('delete_picture/<int:picture_id>/', views.delete_picture, name='delete_picture'),
]
