from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.contrib import auth
from apps.appUsers.models import UserApp
from django.contrib.auth.models import User


"""module responsible for performing tasks related to AppUser in a decentralized way"""


def check_field_empty(field):
    #checks if the passed string is an empty value
    
    return not field.strip()

def check_equality(data1, data2):
    #double field check

    if check_field_empty(data1) or check_field_empty(data2):
        return True
    
    return data1 != data2

def execute_login(request, user_login, user_password):
    #start session

    user = auth.authenticate(request, username=user_login, password=user_password)

    if user is not None:
        auth.login(request, user)

        return True
    
    else:
        return False

def check_user(user_login):
    #check if there is a user

    if User.objects.filter(email=user_login).exists():
        
         # O parâmetro flat = True garante que apenas o campo username será o resultado
        return User.objects.filter(email=user_login).values_list('username', flat=True).get()  
       
    else:
        return False

def get_user(request):
    #search user e return if exist

    return get_object_or_404(User, pk=request.user.id)

def factor_user(data_user):
    #new user factory
  
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
    