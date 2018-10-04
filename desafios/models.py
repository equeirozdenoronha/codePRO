import uuid
from django.contrib.auth.models import User
from django.db import models
from usuarios.models import *

class Academico(models.Model):

    CGU = models.CharField(max_length=9, null=True)
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    pontuacao = models.IntegerField(null=True)

    class Meta:
        ordering = ['pontuacao']

    def __str__(self):

        return "{} ({})".format(self.usuario.nome.upper(), self.usuario.email)

class Pergunta(models.Model):

    FACIL = 1
    MEDIA = 2
    DIFICIL = 3

    NIVEL = (
        (FACIL, ('Fácil')),
        (MEDIA, ('Média')),
        (DIFICIL, ('Difícil')),
    )

    A = "A"
    B = "B"
    C = "C"
    D = "D"
    ALTERNATIVAS = (
        (A, 'A'),
        (B, 'B'),
        (C, 'C'),
        (D, 'D'),
    )
    codigo = models.UUIDField(default=uuid.uuid4, primary_key=True)
    enunciado = models.TextField(max_length=1000, null=True)
    alternativaA = models.TextField(max_length=500, null=True)
    alternativaB = models.TextField(max_length=500, null=True)
    alternativaC = models.TextField(max_length=500, null=True)
    alternativaD = models.TextField(max_length=500, null=True)
    alternativa_certa = models.CharField(max_length=2, choices=ALTERNATIVAS)
    nivel = models.IntegerField(choices=NIVEL, default=FACIL)

    class Meta:
        ordering = ['enunciado']

    def __str__(self):

        return "{}".format(self.enunciado)

class Resposta(models.Model):

    resposta = models.CharField(max_length=5, null=True)
    academico = models.ForeignKey(Academico, on_delete=models.CASCADE)
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE)