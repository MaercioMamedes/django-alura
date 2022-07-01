from django.shortcuts import render, get_object_or_404
from .models import Recipe


# views of app.

def index(request):
    recipe_list = Recipe.objects.order_by('date_recipe').filter(published=True)

    recipe_list_show = {
        'recipe_list': recipe_list
    }

    return render(request, 'appCore/index.html', recipe_list_show)


def recipe(request, recipe_id):
    recipe_object = get_object_or_404(Recipe, pk=recipe_id)
    recipe_show = {
        'recipe': recipe_object,
    }

    return render(request, 'appCore/receita.html', recipe_show)


def search(request):
    recipe_list = Recipe.objects.order_by('date_recipe').filter(published=True)

    if 'search' in request.GET:
        name_to_search = request.GET['search']

        if search:
            recipe_list = recipe_list.filter(name_recipe__icontains=name_to_search)

    recipe_list_show = {
        'recipe_list': recipe_list
    }

    return render(request, 'index.html', recipe_list_show)
