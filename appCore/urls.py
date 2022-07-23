from django.urls import path
#from django.contrib import admin
from . import views



urlpatterns = [
    path('', views.index, name='index'),
    path('<int:recipe_id>', views.recipe, name='recipe'),
    path('buscar', views.search, name='search'),
  #  path('admin', admin.site.urls)

]
