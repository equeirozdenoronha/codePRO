# api/urls.py
from django.urls import include, path
from desafios.views import *

urlpatterns = [
    path('academicos/', AcademicoListView.as_view()),
    path('perguntas/', PerguntaListView.as_view()),
    path('respostas/', RespostaListView.as_view())
]