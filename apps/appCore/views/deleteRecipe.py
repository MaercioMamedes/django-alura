from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from apps.appCore.models import Recipe
from apps.appUsers.models import UserApp
from apps.appUsers.helpers import get_user
import os

"""View responsible for processing, rendering and deleting the Recipes model"""


def delete_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    recipe.delete()
    abs_path = os.path.dirname(os.path.abspath('__file__')) + recipe.picture_recipe.url

    os.remove(abs_path)

    user = get_user(request)
    user_app = get_object_or_404(UserApp, user=user.id)
    user_app.qtd_recipe -= 1
    user_app.save()

    messages.info(request, "Receita excluída com sucesso")

    return redirect('dashboard')
