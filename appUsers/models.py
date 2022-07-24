from django.db import models
from django.contrib.auth.models import User


class UserApp(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField('Nome Completo', max_length=200)
    qtd_recipe = models.IntegerField('Quantidade de Receitas', default=0)

    def __str__(self):
        return self.full_name
