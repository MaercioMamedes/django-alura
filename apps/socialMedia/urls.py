from django.urls import path
from apps.socialMedia.views.rank import *

urlpatterns = [
    path('teste', teste, name='teste' )
]
