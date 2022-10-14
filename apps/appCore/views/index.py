from django.shortcuts import render
from apps.appCore.models import Recipe
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


""""Index page, responsible for loading all published recipes, 
following the pagination configuration of 3 recipes per page."""


def index(request):
    recipe_list = Recipe.objects.order_by('-date_recipe').filter(published=True)

    # recipe pagination structure
    
    paginator = Paginator(recipe_list, 3)
    page = request.GET.get('page')
    recipe_per_page = paginator.get_page(page)

    # end Pagination struct

    recipe_list_show = {
        'recipe_list': recipe_per_page
    }

    return render(request, 'appCore/index.html', recipe_list_show)
