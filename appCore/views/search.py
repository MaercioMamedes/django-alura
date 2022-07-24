from django.shortcuts import render
from appCore.models import Recipe


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
