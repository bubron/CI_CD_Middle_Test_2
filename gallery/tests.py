from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import Category, Image
from django.utils import timezone

class CategoryModelTest(TestCase):
    def test_category_creation(self):
        category = Category.objects.create(name="Природа")
        self.assertEqual(str(category), "Природа")
        self.assertEqual(Category.objects.count(), 1)