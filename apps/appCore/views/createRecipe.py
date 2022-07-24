from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from appUsers.helpers import get_user
from appUsers.models import UserApp
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
        published        = request.POST['published']
        user             = get_user(request)

        recipe = Recipe.objects.create(
            user              = user,
            name_recipe       = name_recipe,
            ingredients       = ingredients, 
            preparation_mode  = preparation_mode,
            preparation_time  = preparation_time, 
            efficiency        = efficiency,
            category          = category, 
            picture_recipe    = picture_recipe,
            published         = published
            )


        user_app = get_object_or_404(UserApp,user=user.id)
        user_app.qtd_recipe += 1
        user_app.save()

        recipe.save()

        

        messages.success(request, 'Receita criada com sucesso !')

        return redirect('dashboard')

    else:

        return render(request, 'appCore/create_recipe.html')
