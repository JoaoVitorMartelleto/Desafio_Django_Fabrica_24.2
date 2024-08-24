from django.shortcuts import render, get_object_or_404, redirect
from .models import Livro, Usuario
from .forms import LivroForm, UsuarioForm, LivroAPIForm
from .api import obter_detalhes_livro


def listarLivros(request):
    livros = Livro.objects.all()
    return render(request, 'livros/listarLivros.html', {'livros': livros})

def detalharLivro(request, isbn):
    livro = get_object_or_404(Livro, isbn=isbn)
    return render(request, 'livros/detalharLivro.html', {'livro': livro})

def criarLivro(request):
    if request.method == 'POST':
        form = LivroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('livros:listarLivros')
    else:
        form = LivroForm()
    return render(request, 'livros/formLivro.html', {'form': form})

def editarLivro(request, isbn):
    livro = get_object_or_404(Livro, isbn=isbn)
    if request.method == 'POST':
        form = LivroForm(request.POST, instance=livro)
        if form.is_valid():
            form.save()
            return redirect('livros:listarLivros')
    else:
        form = LivroForm(instance=livro)
    return render(request, 'livros/formLivro.html', {'form': form})

def excluirLivro(request, isbn):
    livro = get_object_or_404(Livro, isbn=isbn)
    if request.method == 'POST':
        livro.delete()
        return redirect('livros:listarLivros')
    return render(request, 'livros/confirmarExclusao.html', {'livro': livro})

def adicionarLivroComApi(request):
    if request.method == 'POST':
        form = LivroAPIForm(request.POST)
        if form.is_valid():
            isbn = form.cleaned_data['isbn']
            dados_livro = obter_detalhes_livro(isbn)

            if not dados_livro:
                form.add_error('isbn', 'Livro não encontrado ou erro ao acessar a API.')
            else:
                livro = Livro(
                    titulo=dados_livro.get('title', ''),
                    autor=dados_livro.get('authors', [{}])[0].get('name', ''),
                    isbn=isbn,
                    descricao=dados_livro.get('description', ''),
                    data_publi=dados_livro.get('publish_date', None)
                )
                livro.save()
                return redirect('livros:listarLivros')
    else:
        form = LivroAPIForm()
    return render(request, 'livros/formLivroComApi.html', {'form': form})


def listaUser(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuarios/listaUser.html', {'usuarios': usuarios})

def detalharUser(request, usuarioId):
    usuario = get_object_or_404(Usuario, id=usuarioId)
    return render(request, 'usuarios/detalharUser.html', {'usuario': usuario})

def criarUser(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('usuarios:listaUser')
    else:
        form = UsuarioForm()
    return render(request, 'usuarios/formUser.html', {'form': form})

def editarUser(request, usuarioId):
    usuario = get_object_or_404(Usuario, id=usuarioId)
    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('usuarios:listaUser')
    else:
        form = UsuarioForm(instance=usuario)
    return render(request, 'usuarios/formUser.html', {'form': form})

def excluirUser(request, usuarioId):
    usuario = get_object_or_404(Usuario, id=usuarioId)
    if request.method == 'POST':
        usuario.delete()
        return redirect('usuarios:listaUser')
    return render(request, 'usuarios/confirmarExclusao.html', {'usuario': usuario})
