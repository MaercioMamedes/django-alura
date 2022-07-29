from django.urls import path
from appUsers.views import *

"""Routing appCore views"""

urlpatterns = [
    path('register', register, name='register'),
    path('login', login, name='login'),
    path('logout', logout, name='logout'),
    path('dashboard', dashboard, name='dashboard'),
    path('update', update_start, name='update_start'),
    path('update-user', update_finish, name='update_finish'),
]