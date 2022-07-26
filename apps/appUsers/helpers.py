from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.contrib import auth
from appUsers.models import UserApp
from django.contrib.auth.models import User



"""Checar campo em branco"""

def check_field_empty(field):
    return not field.strip()

""" verificação de dois fatores de cadastro """
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

"""Fábrica de usuários"""

def factor_user(data_user):
  
    """data_user = (full_name, user_name, email, password)"""   #metadata

    first_name = data_user[0].split()[0]

    last_name = data_user[0].split()[-1]

    new_user = User.objects.create_user(username=data_user[1], 
                                        email   =data_user[2],
                                        password=data_user[3],
                                        first_name=first_name,
                                        last_name=last_name,
                                        )
    new_user.save()

    new_user_app = UserApp(user=new_user, full_name=data_user[0])

    new_user_app.save()
    