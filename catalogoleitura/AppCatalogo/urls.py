from django.urls import path
from . import views

app_name = 'livros'

urlpatterns = [
    path('livros/', views.listarLivros, name='listarLivros'),
    path('livros/formLivro.html', views.criarLivro, name='criarLivro'),
    path('livros/formLivroComApi.html', views.adicionarLivroComApi, name='adicionarLivroComApi'),  
    path('livros/<str:isbn>', views.detalharLivro, name='detalharLivro'),
    path('livros/editar/<str:isbn>/', views.editarLivro, name='editarLivro'),
    path('livros/excluir/<str:isbn>/', views.excluirLivro, name='excluirLivro'),

    path('usuario/', views.listaUser, name='listaUser'),
    path('usuario/<int:usuarioId>/', views.detalharUser, name='detalharUser'),
    path('usuario/criar/', views.criarUser, name='criarUser'),
    path('usuario/<int:usuarioId>/editar/', views.editarUser, name='editarUser'),
    path('usuario/<int:usuarioId>/excluir/', views.excluirUser, name='excluirUser'),
]
