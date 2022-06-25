from django.db import models
from datetime import datetime


class Recipe(models.Model):
    name_recipe = models.CharField('Receita', max_length=200)
    ingredients = models.TextField('Ingredientes')
    preparation_mode = models.TextField('Modo de Preparo')
    preparation_time = models.IntegerField('Tempo de Preparo')
    efficiency = models.CharField('Rendimento', max_length=100)
    category = models.CharField('Categoria', max_length=100)
    date_recipe = models.DateTimeField('data da publicação', default=datetime.now, blank=True)

