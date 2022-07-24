from django.shortcuts import  redirect, render
from appCore.models import Recipe

def dashboard(request):

    if request.user.is_authenticated:
        id = request.user.id
        recipes = Recipe.objects.order_by('-date_recipe').filter(user=id)
        
        data = { 
            'recipes' : recipes
        }
        return render(request, 'appUsers/dashboard.html', data)
    else:
        return redirect('index')
