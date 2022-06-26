from django.shortcuts import render, get_object_or_404
from .models import Recipe


# views of app.

def index(request):
    recipe_list = Recipe.objects.order_by('-date_recipe').filter(published=True)
    recipe_list_show = {
        'recipe_list': recipe_list
    }

    return render(request, 'index.html', recipe_list_show)


def recipe(request, recipe_id):
    recipe_object = get_object_or_404(Recipe, pk=recipe_id)
    recipe_show = {
        'recipe': recipe_object,
    }

    return render(request, 'receita.html', recipe_show)
