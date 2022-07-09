from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.contrib import auth


"""Checar campo em branco e verificação de dois fatores de cadastro"""

def check_field_empty(field):
    return not field.strip()

def check_equality(data1, data2):
    if check_field_empty(data1) or check_field_empty(data2):
        return True
    
    return data1 != data2


"""Login em sessão"""

def execute_login(request, user_login, user_password):
    user = auth.authenticate(request, username=user_login, password=user_password)

    if user is not None:
        auth.login(request, user)

        return True
    
    else:
        return False



"""Verifica se existe usuário"""

def check_user(user_login):
    if User.objects.filter(email=user_login).exists():
        
         # O parâmetro flat = True garante que apenas o campo username será o resultado
        return User.objects.filter(email=user_login).values_list('username', flat=True).get()  
       

    else:
        return False

"""Retorna Usuário"""

def get_user(request):
    return get_object_or_404(User, pk=request.user.id)