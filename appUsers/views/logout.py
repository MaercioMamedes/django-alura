from django.shortcuts import redirect
from django.contrib import messages, auth


def logout(request):
    auth.logout(request)
    messages.info(request, 'Logout realizado com sucesso !')

    return redirect('index')
