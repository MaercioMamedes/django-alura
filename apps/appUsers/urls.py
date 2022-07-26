from django.urls import path
from appUsers.views import *


urlpatterns = [
    path('register', register, name='register'),
    path('login', login, name='login'),
    path('logout', logout, name='logout'),
    path('dashboard', dashboard, name='dashboard'),
    path('update', update_start, name='update_start')
]