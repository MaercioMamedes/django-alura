from django.db import models
from django.contrib.auth.models import User


class UserApp(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField('Nome Completo', max_length=200)
    qtd_recipe = models.IntegerField('Quantidade de Receitas', default=0)

    def __str__(self):
        return self.full_name


def factor_user(data_user):
  
    """data_user = (full_name, user_name, email, password)"""   #metadata

    new_user = User.objects.create_user(username=data_user[1], 
                                        email   =data_user[2],
                                        password=data_user[3],
                                        )
    new_user.save()

    new_user_app = UserApp(user=new_user, full_name=data_user[0])

    new_user_app.save()

