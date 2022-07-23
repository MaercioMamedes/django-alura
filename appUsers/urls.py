from django.urls import path
from . import views


urlpatterns = [
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('create-recipe', views.create_recipe, name='create_recipe'),
    path('delete/<int:recipe_id>', views.delete_recipe, name='delete_recipe'),
    path('update-recipe/<int:recipe_id>', views.start_update_recipe, name='start_update_recipe'),
    path('update-recipe', views.finished_update_recipe, name='finished_update_recipe'),
]