from appUsers.helpers import get_user
from appUsers.models import UserApp
from django.shortcuts import get_object_or_404, render

def update_start(request):
    user = get_user(request)
    user_app = get_object_or_404(UserApp, user=user.id)

    data_user = {
        'user' : user,
        'user_app' : user_app,
    }

    return render(request, 'appUsers/update_user.html', data_user)


def update_finish(request):

    if request.method == 'POST':


        user = get_user(request)
        user_app = get_object_or_404(UserApp, user=user.id)

        

        data_user = {
            'user' : user,
            'user_app' : user_app,
        }

