"""
URL configuration for recipe_help project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework import routers

from recipes.views import index, category_recipes, UserRecipeRelationView,SearchView
from django.conf.urls.static import static
from django.conf import settings



router = routers.SimpleRouter()
router.register(r'relation', UserRecipeRelationView)
#router.register(r'categories', CategoriesViewSet)'''


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('category/<int:category_id>/', category_recipes, name='category_recipes'),
    path('search/', SearchView.as_view(), name='search'),
    #path('relation', UserRecipeRelationView.as_view, name='relation_user')

    #path('category/<int:category_id>/', RecipesViewSets.as_view(), name='category'),
]

urlpatterns += router.urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


