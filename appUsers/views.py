from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages, auth
from . import helpers
from . import models
from appCore.models import *


def register(request):

    if request.method == 'POST':
        name = request.POST['fullname']
        user_name = request.POST['user_name']
        email = request.POST['email']
        email_confirm = request.POST['email_confirm']
        password = request.POST['password']
        password_confirm = request.POST['password_confirm']


        if helpers.check_field_empty(name):
            messages.error(request, 'O campo nome não pode ficar em branco')

            return redirect('register')

        if helpers.check_field_empty(user_name):
            messages.error(request, 'O campo Usuário de login não pode ficar em branco')

            return redirect('register')
        
        if helpers.check_equality(email, email_confirm):
            messages.error(request, 'os campos email e confirmação de email estão vazios ou não são iguais')

            return redirect('register')

        if helpers.check_equality(password, password_confirm):
            messages.error(request, 'os campos senha e confirmação de senha estão vazios ou não são iguais')

            return redirect('register')


        data_user = (name, user_name, email, password)

        models.factor_user(data_user)

        return redirect('login')

    else:

        return render(request, 'appUsers/registerUser.html')

def logout(request):
    auth.logout(request)
    messages.info(request, 'Logout realizado com sucesso !')

    return redirect('index')

def login(request):

    if request.method == 'POST':
        user_login    = request.POST['user_login']
        user_password = request.POST['password']
        type_login    = request.POST['type_login']

        if helpers.check_field_empty(user_login) or helpers.check_field_empty(user_password):
            messages.error(request, 'Os campos email e senhas não podem ficar em branco')

            return redirect('login')
        
        if type_login == 'username':

            if helpers.execute_login(request, user_login, user_password):
                messages.success(request, 'Login realizado com sucesso')

                return redirect('dashboard')

            else:
                messages.error(request, 'Usuário ou senha incorretos')
                return redirect('login')
        
        else:

            username = helpers.check_user(user_login)

            if helpers.execute_login(request, username, user_password):
                messages.success(request, 'Login realizado com sucesso')
                return redirect('dashboard')

            else:
                messages.error(request, 'Usuário ou senha incorretos')
                return redirect('login')
                

    
    return render(request, 'appUsers/login.html')


def create_recipe(request):
    if request.method == 'POST':
        name_recipe      = request.POST['name_recipe']
        ingredients      = request.POST['ingredients']
        preparation_mode = request.POST['preparation_mode']
        preparation_time = request.POST['preparation_time']
        efficiency       = request.POST['efficiency']
        category         = request.POST['category']
        picture_recipe   = request.FILES['picture_recipe']
        user             = helpers.get_user(request)

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

        return redirect('dashboard')

    else:

        return render(request, 'appUsers/create_recipe.html')

def delete_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    recipe.delete()
    
    return redirect('dashboard')


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
            recipe.foto_receita = request.FILES['picture_recipe']

        recipe.save()

    return redirect('dashboard')
    

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


