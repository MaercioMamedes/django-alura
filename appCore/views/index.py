from django.shortcuts import render
from appCore.models import Recipe

def index(request):
    recipe_list = Recipe.objects.order_by('date_recipe').filter(published=True)

    recipe_list_show = {
        'recipe_list': recipe_list
    }

    return render(request, 'appCore/index.html', recipe_list_show)
