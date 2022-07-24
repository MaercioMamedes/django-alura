from django.shortcuts import redirect, render
from django.contrib import messages
from appUsers.helpers import check_field_empty, check_equality, factor_user



def register(request):

    if request.method == 'POST':
        name = request.POST['fullname']
        user_name = request.POST['user_name']
        email = request.POST['email']
        email_confirm = request.POST['email_confirm']
        password = request.POST['password']
        password_confirm = request.POST['password_confirm']


        if check_field_empty(name):
            messages.error(request, 'O campo nome não pode ficar em branco')

            return redirect('register')

        if check_field_empty(user_name):
            messages.error(request, 'O campo Usuário de login não pode ficar em branco')

            return redirect('register')
        
        if check_equality(email, email_confirm):
            messages.error(request, 'os campos email e confirmação de email estão vazios ou não são iguais')

            return redirect('register')

        if check_equality(password, password_confirm):
            messages.error(request, 'os campos senha e confirmação de senha estão vazios ou não são iguais')

            return redirect('register')


        data_user = (name, user_name, email, password)

        factor_user(data_user)

        messages.success(request, "Usuário criado com sucesso !")
        
        return redirect('login')

    else:

        return render(request, 'appUsers/registerUser.html')
