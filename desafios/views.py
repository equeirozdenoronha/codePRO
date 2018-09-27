from django.shortcuts import render
from rest_framework import generics

from . import models
from . import serializers

class AcademicoListView(generics.ListCreateAPIView):
    queryset = models.Usuario.objects.all()
    serializer_class = serializers.AcademicoSerializer


class PerguntaListView(generics.ListCreateAPIView):
    queryset = models.Pergunta.objects.all()
    serializer_class =  serializers.PerguntaSerializer

class RespostaListView(generics.ListCreateAPIView):
    queryset = models.Resposta.objects.all()
    serializer_class = serializers.RespostaSerializer