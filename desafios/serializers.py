from rest_framework import serializers
from desafios.models import *

class AcademicoSerializer(serializers.Serializer):

    id = serializers.IntegerField()
    usuario = serializers.SlugRelatedField(read_only=True, slug_field="nome")
    pontuacao = serializers.IntegerField()


    def create(self, validated_data):
        return Academico.objects.create(**validated_data)

    def update(self, instance, validated_data):

        instance.nome = validated_data.get('nome', instance.nome)
        instance.pontuacao = validated_data.get('pontuacao', instance.funcao)

        instance.save()
        return instance

    class Meta:
        model = Academico
        fields = [
            'id',
            'usuario',
            'pontuacao',
        ]


class PerguntaSerializer(serializers.Serializer):

    codigo = serializers.UUIDField()
    enunciado = serializers.CharField()
    alternativaA = serializers.CharField()
    alternativaB = serializers.CharField()
    alternativaC = serializers.CharField()
    alternativaD = serializers.CharField()
    alternativa_certa = serializers.CharField()
    nivel = serializers.IntegerField()

    def create(self, validated_data):
        return Pergunta.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.enunciado = validated_data.get('enunciado', instance.enunciado)
        instance.alternativaA = validated_data.get('alternativaA', instance.alternativaA)
        instance.alternativaB = validated_data.get('alternativaB', instance.alternativaB)
        instance.alternativaC = validated_data.get('alternativaC', instance.alternativaC)
        instance.alternativaD = validated_data.get('alternativaD', instance.alternativaD)
        instance.alternativa_certa = validated_data.get('alternativa_certa', instance.alternativa_certa)
        instance.nivel = validated_data.get('nivel', instance.nivel)

        instance.save()
        return instance

    class Meta:
        model = Pergunta
        fields = [
            'enunciado',
            'alternativaA',
            'alternativaB',
            'alternativaC',
            'alternativaD',
            'alternativa_certa',
            'nivel'
        ]


class RespostaSerializer(serializers.Serializer):

    resposta = serializers.CharField()
    academico = serializers.SlugRelatedField(read_only=True, slug_field="nome")
    pergunta = serializers.SlugRelatedField(read_only=True, slug_field="enunciado")


    def create(self, validated_data):
        return Pergunta.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.resposta = validated_data.get('resposta', instance.resposta)
        instance.save()
        return instance

    class Meta:
        model = Pergunta
        fields = [
            'pergunta',
            'resposta',
            'academico',
            ]