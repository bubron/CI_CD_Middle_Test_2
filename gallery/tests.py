from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import Category, Image
from django.utils import timezone

class CategoryModelTest(TestCase):
    def test_category_creation(self):
        category = Category.objects.create(name="Природа")
        self.assertEqual(str(category), "Природа")
        self.assertEqual(Category.objects.count(), 1)

class ImageModelTest(TestCase):
    def setUp(self):
        self.category1 = Category.objects.create(name="Природа")
        self.category2 = Category.objects.create(name="Міста")
        
        test_image = SimpleUploadedFile(
            name='test_image.jpg',
            content=b'',
            content_type='image/jpeg'
        )
        
        self.image = Image.objects.create(
            title="Тестове зображення",
            image=test_image,
            created_date=timezone.now().date(),
            age_limit=12
        )
        self.image.categories.add(self.category1, self.category2)
