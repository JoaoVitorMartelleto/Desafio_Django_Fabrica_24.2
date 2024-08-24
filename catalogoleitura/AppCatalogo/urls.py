from django.urls import path
from . import views

app_name = 'livros'

urlpatterns = [
    path('template/livros/', views.listarLivros, name='listarLivros'),
    path('template/livros/formLivro.html', views.criarLivro, name='criarLivro'),
    path('template/livros/formLivroComApi.html', views.adicionarLivroComApi, name='adicionarLivroComApi'),  
    path('template/livros/<str:isbn>', views.detalharLivro, name='detalharLivro'),
    path('template/livros/editar/<str:isbn>/', views.editarLivro, name='editarLivro'),
    path('template/livros/excluir/<str:isbn>/', views.excluirLivro, name='excluirLivro'),

    path('template/usuarios/listar/', views.listaUser, name='listaUser'),
    path('template/usuarios/<int:usuarioId>/', views.detalharUser, name='detalharUser'),
    path('template/usuarios/criar/', views.criarUser, name='criarUser'),
    path('template/usuarios/<int:usuarioId>/editar/', views.editarUser, name='editarUser'),
    path('template/usuarios/<int:usuarioId>/excluir/', views.excluirUser, name='excluirUser'),
]
