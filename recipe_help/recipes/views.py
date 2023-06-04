from django.shortcuts import render
from django.views.generic import ListView
from rest_framework import generics
from rest_framework.mixins import UpdateModelMixin
from rest_framework.viewsets import GenericViewSet

from recipes.serializers import SerializersRecipe, SerializersCategories, UserRecipeRelationSerializer
from .models import RecipesModel, CategoriesModel, UserRecipeRelation


# class IndexViewSets(TemplateView):
# template_name = 'recipes/index.html'


def index(request):
    context = {
        'recipes': RecipesModel.objects.all(),
        'category': CategoriesModel.objects.all(),
    }
    return render(request, 'recipes/index.html', context)


def category_recipes(request, category_id):
    category = CategoriesModel.objects.get(id=category_id)
    recipes = RecipesModel.objects.filter(category=category)
    return render(request, 'recipes/category.html', {'category': category, 'recipes': recipes})


'''class RecipeListView(generics.ListAPIView):
    queryset = RecipesModel.objects.all()
    serializer_class = SerializersRecipe
    search_fields = ['name', 'description', 'products']'''


class UserRecipeRelationView(UpdateModelMixin, GenericViewSet):
    queryset = UserRecipeRelation.objects.all()
    serializer_class = UserRecipeRelationSerializer
    lookup_field = 'recipe'

    def get_object(self):
        obj, created = UserRecipeRelation.objects.get_or_create(user=self.request.user,
                                                                recipe_id=self.kwargs['book'])

        return obj


class SearchView(ListView):
    model = RecipesModel
    template_name = 'recipes/search_results.html'
    context_object_name = 'recipes_search'

    def get_queryset(self):

        return RecipesModel.objects.filter(products__icontains=self.request.GET.get('q'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context





'''class RecipesViewSets(ListView):
    model = RecipesModel
    template_name = 'recipes/category.html'

    def get_queryset(self):
        queryset = super(RecipesViewSets, self).get_queryset()
        category_id = self.kwargs.get('category_id')
        return queryset.filter(category_id=category_id) if category_id else queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(RecipesViewSets, self).get_context_data()
        context['categories'] = CategoriesModel.objects.all()
        return context'''

'''def category_recipes(request, category_id):
    category = CategoriesModel.objects.get(id=category_id)
    recipes = RecipesModel.objects.filter(category=category)
    return render(request, 'recipes/category.html', {'recipes': recipes})'''
