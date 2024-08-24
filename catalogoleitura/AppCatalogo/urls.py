# AppCatalogo/urls.py

from django.urls import path
from . import views

app_name = 'livros'

urlpatterns = [
    path('', views.listarLivros, name='listarLivros'),
    path('adicionar/manual/', views.criarLivro, name='criarLivro'),
    path('adicionar/api/', views.adicionarLivroComApi, name='adicionarLivroComApi'),
    path('<str:isbn>/', views.detalharLivro, name='detalharLivro'),
    path('<str:isbn>/editar/', views.editarLivro, name='editarLivro'),
    path('<str:isbn>/excluir/', views.excluirLivro, name='excluirLivro'),

    path('usuarios/', views.listaUser, name='listaUser'),
    path('usuarios/<int:usuarioId>/', views.detalharUser, name='detalharUser'),
    path('usuarios/criar/', views.criarUser, name='criarUser'),
    path('usuarios/<int:usuarioId>/editar/', views.editarUser, name='editarUser'),
    path('usuarios/<int:usuarioId>/excluir/', views.excluirUser, name='excluirUser'),
]
