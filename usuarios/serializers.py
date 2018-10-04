# users/serializers.py
from rest_framework import serializers
from . import models

class UserSerializer(serializers.ModelSerializer):

    nome = serializers.CharField()
    class Meta:
        model = models.Usuario
        fields = ('email', 'username','nome')