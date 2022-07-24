from django.shortcuts import redirect, render
from django.contrib import messages
from appUsers.helpers import get_user
from appCore.models import Recipe


def create_recipe(request):
    if request.method == 'POST':
        name_recipe      = request.POST['name_recipe']
        ingredients      = request.POST['ingredients']
        preparation_mode = request.POST['preparation_mode']
        preparation_time = request.POST['preparation_time']
        efficiency       = request.POST['efficiency']
        category         = request.POST['category']
        picture_recipe   = request.FILES['picture_recipe']
        user             = get_user(request)

        recipe = Recipe.objects.create(
            user              = user,
            name_recipe       = name_recipe,
            ingredients       = ingredients, 
            preparation_mode  = preparation_mode,
            preparation_time  = preparation_time, 
            efficiency        = efficiency,
            category          = category, 
            picture_recipe    = picture_recipe)

        recipe.save()

        messages.success(request, 'Receita criada com sucesso !')

        return redirect('dashboard')

    else:

        return render(request, 'appUsers/create_recipe.html')
