from django.shortcuts import render, get_object_or_404
from apps.appCore.models import Recipe

"""view responsible for create Recipe"""


def recipe(request, recipe_id):
    recipe_object = get_object_or_404(Recipe, pk=recipe_id)
    recipe_show = {
        'recipe': recipe_object,
    }

    return render(request, 'appCore/receita.html', recipe_show)
