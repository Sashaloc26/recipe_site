from django.contrib import admin
from .models import RecipesModel, CategoriesModel, UserRecipeRelation

admin.site.register(RecipesModel)
admin.site.register(CategoriesModel)
admin.site.register(UserRecipeRelation)