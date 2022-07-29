from django.shortcuts import redirect, render
from django.contrib import messages
from appUsers.helpers import check_field_empty, execute_login, check_user #the functions check_field_empty, execute_login, check_user, are their own methods


"""view responsible for handling the login"""

def login(request):

    if request.method == 'POST':
        user_login    = request.POST['user_login']
        user_password = request.POST['password']
        type_login    = request.POST['type_login']

        if check_field_empty(user_login) or check_field_empty(user_password):
            messages.error(request, 'Os campos email e senhas não podem ficar em branco')

            return redirect('login')
        
        if type_login == 'username':

            if execute_login(request, user_login, user_password):
                messages.success(request, 'Login realizado com sucesso')

                return redirect('dashboard')

            else:
                messages.error(request, 'Usuário ou senha incorretos')
                return redirect('login')
        
        else:

            username = check_user(user_login)

            if execute_login(request, username, user_password):
                messages.success(request, 'Login realizado com sucesso')
                return redirect('dashboard')

            else:
                messages.error(request, 'Usuário ou senha incorretos')
                return redirect('login')
                
    return render(request, 'appUsers/login.html')
    