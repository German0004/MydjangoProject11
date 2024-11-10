from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
class Picture(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="pictures"
    )
    image = models.ImageField(
        upload_to="pictures/"
    )  # Зберігаємо картинки у media/pictures
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title
