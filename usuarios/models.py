from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):

    nome = models.CharField(blank=True, max_length=255)

    def __str__(self):
        return '{}({})'.format(self.nome, self.email)
