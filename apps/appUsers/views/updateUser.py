from appUsers.helpers import get_user
from appUsers.models import UserApp
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages, auth
from appUsers.helpers import check_field_empty, check_equality #this functions are their own methods


"""views responsible for rendering and processing user data updates"""

def update_start(request):

    # Rendering user data

    user = get_user(request)
    user_app = get_object_or_404(UserApp, user=user.id)

    data_user = {
        'user' : user,
        'user_app' : user_app,
    }

    return render(request, 'appUsers/update_user.html', data_user)


def update_finish(request):

    # Processing user data

    if request.method == 'POST':

        user = get_user(request)
        user_app = get_object_or_404(UserApp, user=user.id)

        if user.username != auth.authenticate(request, username=user.username, password=request.POST['password']).username:

            messages.error(request, 'senha inválida')
            return redirect ('update_start')

        else:
            name = request.POST['fullname']
            user_name = request.POST['user_name']
            email = request.POST['email']
            email_confirm = request.POST['email_confirm']

            if check_field_empty(name):
                messages.error(request, 'O campo nome não pode ficar em branco')

                return redirect('update_start')

            if check_field_empty(user_name):
                messages.error(request, 'O campo Usuário de login não pode ficar em branco')

                return redirect('update_start')
            
            if check_equality(email, email_confirm):
                messages.error(request, 'os campos email e confirmação de email estão vazios ou não são iguais')

                return redirect('update_start')

            if user.username != user_name:

                user.username = user_name
                user.save()
            
            if user.email != email:
                user.email = email


            if user_app.full_name != name:

                user_app.full_name = name
                user_app.save()

                user.first_name = name.split()[0]
                user.last_name = name.split()[-1]
                user.save()
            
            messages.success(request, 'Dados alterados com sucesso')

    return redirect('dashboard')
    
