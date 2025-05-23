from django.db import models
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Назва категорії")

    class Meta:
        verbose_name = "Категорія"
        verbose_name_plural = "Категорії"

    def __str__(self):
        return self.name

class Image(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    image = models.ImageField(upload_to='images/', verbose_name="Зображення")
    categories = models.ManyToManyField(Category, verbose_name="Категорії")
    created_date = models.DateField(default=timezone.now, verbose_name="Дата створення")
    age_limit = models.PositiveIntegerField(default=0, verbose_name="Вікове обмеження")

    class Meta:
        verbose_name = "Зображення"
        verbose_name_plural = "Зображення"

    def __str__(self):
        return self.title