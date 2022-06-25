from django.db import models


class User(models.Model):
    name = models.CharField('Nome', max_length=200)
    email = models.CharField('E-mail', max_length=200)

    def __str__(self):
        return self.name
