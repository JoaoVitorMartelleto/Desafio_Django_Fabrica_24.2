from django.shortcuts import render, get_object_or_404, redirect
from .models import Livro
from .forms import LivroForm
from .forms import UsuarioForm
from .models import Usuario

def listar_livros(request):
    livros = Livro.objects.all()
    return render(request, 'livros/listar_livros.html', {'livros': livros})

def detalhar_livro(request, livro_id):
    livro = get_object_or_404(Livro, isbn = isbn)
    return render(request, 'livros/detalhar_livro.html', {'livro': livro})

def criar_livro(request):
    if request.method == 'POST':
        form = LivroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_livros')
    else:
        form = LivroForm()
    return render(request, 'livros/form_livro.html', {'form': form})

def editar_livro(request, livro_id):
    livro = get_object_or_404(Livro, id=livro_id)
    if request.method == 'POST':
        form = LivroForm(request.POST, instance=livro)
        if form.is_valid():
            form.save()
            return redirect('listar_livros')
    else:
        form = LivroForm(instance=livro)
    return render(request, 'livros/form_livro.html', {'form': form})

def excluir_livro(request, livro_id):
    livro = get_object_or_404(Livro, id=livro_id)
    if request.method == 'POST':
        livro.delete()
        return redirect('listar_livros')
    return render(request, 'livros/confirmar_exclusao.html', {'livro': livro})

def listar_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuarios/listar_usuarios.html', {'usuarios': usuarios})

def detalhar_usuario(request, usuario_id):
    usuario = get_object_or_404(Usuario, id=usuario_id)
    return render(request, 'usuarios/detalhar_usuario.html', {'usuario': usuario})

def criar_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_usuarios')
    else:
        form = UsuarioForm()
    return render(request, 'usuarios/form_usuario.html', {'form': form})


def editar_usuario(request, usuario_id):
    usuario = get_object_or_404(Usuario, id=usuario_id)
    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('listar_usuarios')
    else:
        form = UsuarioForm(instance=usuario)
    return render(request, 'usuarios/form_usuario.html', {'form': form})

def excluir_usuario(request, usuario_id):
    usuario = get_object_or_404(Usuario, id=usuario_id)
    if request.method == 'POST':
        usuario.delete()
        return redirect('listar_usuarios')
    return render(request, 'usuarios/confirmar_exclusao.html', {'usuario': usuario})