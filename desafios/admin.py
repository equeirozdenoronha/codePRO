from django.contrib import admin
from desafios.models import *

class AcademicoAdmin(admin.ModelAdmin):
    model = Academico
    list_display = ['CGU','usuario', 'pontuacao']
    search_fields = ('CGU','pontuacao')
    list_filter = ('CGU', 'pontuacao')
    list_per_page = 30

class PerguntaAdmin(admin.ModelAdmin):
    model = Pergunta
    list_display = ['codigo', 'enunciado', 'nivel']
    search_fields = ('enunciado', 'nivel')
    list_filter = ('enunciado', 'nivel')
    list_per_page = 30

class RespostaAdmin(admin.ModelAdmin):
    model = Resposta
    list_display = ['resposta', 'academico', 'pergunta']
    search_fields = ('resposta', 'academico')
    list_filter = ('resposta', 'academico')
    list_per_page = 30

admin.site.register(Academico, AcademicoAdmin)
admin.site.register(Pergunta, PerguntaAdmin)
admin.site.register(Resposta, RespostaAdmin)
