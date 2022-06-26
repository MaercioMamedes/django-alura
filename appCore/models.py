from django.db import models
from datetime import datetime
from appUsers.models import User


class Recipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name_recipe = models.CharField('Receita', max_length=200)
    ingredients = models.TextField('Ingredientes')
    preparation_mode = models.TextField('Modo de Preparo')
    preparation_time = models.IntegerField('Tempo de Preparo')
    efficiency = models.CharField('Rendimento', max_length=100)
    category = models.CharField('Categoria', max_length=100)
    date_recipe = models.DateTimeField('data da publicação', default=datetime.now, blank=True)

    def __str__(self):
        return self.name_recipe

