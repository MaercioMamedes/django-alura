from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from appCore.models import Recipe


def delete_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    recipe.delete()
    messages.info(request, "Receita excluída com sucesso")
    
    return redirect('dashboard')