from django.shortcuts import render
from appCore.models import Recipe
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):
    print(dir(request.user))
    recipe_list = Recipe.objects.order_by('-date_recipe').filter(published=True)
    paginator = Paginator(recipe_list, 3)
    page = request.GET.get('page')
    recipe_per_page = paginator.get_page(page)

    recipe_list_show = {
        'recipe_list': recipe_per_page
    }

    return render(request, 'appCore/index.html', recipe_list_show)
