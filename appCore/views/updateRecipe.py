from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from appCore.models import Recipe



def start_update_recipe(request, recipe_id):

        recipe = get_object_or_404(Recipe, pk=recipe_id)

        data_ricipe = { 'recipe':recipe}
    
        return render(request, 'appUsers/update_recipe.html', data_ricipe)

def finished_update_recipe(request):

    if request.method == 'POST':
           
        id = request.POST['recipe_id']
        recipe = Recipe.objects.get(pk=id)
        recipe.name_recipe = request.POST['name_recipe']
        recipe.ingredients = request.POST['ingredients']
        recipe.preparation_mode = request.POST['preparation_mode']
        recipe.preparation_time = request.POST['preparation_time']
        recipe.efficiency = request.POST['efficiency']
        recipe.category = request.POST['category']
        recipe.published = request.POST['published']

        if 'picture_recipe' in request.FILES:
            recipe.picture_recipe = request.FILES['picture_recipe']

        recipe.save()

        messages.success(request, "receita atualizada com sucesso")

    return redirect('dashboard')