import json
from django.shortcuts import render
from appUsers.models import UserApp


def ranking(request):

    data_users = UserApp.objects.order_by('-qtd_recipe')

    lists_users = {
        'data_users' : data_users
    }

    return render(request, 'socialMedia/ranking.html', lists_users)
