from django.contrib import admin
from .models import Category, Image

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_date', 'age_limit')
    filter_horizontal = ('categories',)