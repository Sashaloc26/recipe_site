from http import HTTPStatus
from django.test import TestCase
from django.urls import reverse
from .models import CategoriesModel
from recipes.views import category_recipes


class IndexViewTestCase(TestCase):

    def test_view(self):
        path = reverse('index')
        response = self.client.get(path)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'recipes/index.html')


class RecipeViewTestCase(TestCase):
    def setUp(self):
        self.categor = CategoriesModel.objects.all()

    def test_list(self):

        path = reverse('index')
        response = self.client.get(path)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.category, self.categor)
        #self.assertTemplateUsed(response, 'recipes/category.html')
