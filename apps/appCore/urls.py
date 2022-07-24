from django.urls import path
from appCore.views import *


urlpatterns = [
    path('', index, name='index'),
    path('<int:recipe_id>', recipe, name='recipe'),
    path('buscar', search, name='search'),
    path('create-recipe', create_recipe, name='create_recipe'),
    path('delete/<int:recipe_id>', delete_recipe, name='delete_recipe'),
    path('update-recipe/<int:recipe_id>', start_update_recipe, name='start_update_recipe'),
    path('update-recipe', finished_update_recipe, name='finished_update_recipe'),

]
