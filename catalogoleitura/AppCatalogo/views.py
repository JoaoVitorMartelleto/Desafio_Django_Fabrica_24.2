from django.shortcuts import render, get_object_or_404, redirect
from .models import Livro, Usuario
from .forms import LivroForm, UsuarioForm, LivroAPIForm
import requests
from datetime import datetime

def listarLivros(request):
    livros = Livro.objects.all()
    if not livros:  
        livros = None  

    return render(request, 'livros/listarLivro.html', {'livros': livros})


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
            
            url = f"https://openlibrary.org/api/books?bibkeys=ISBN:{isbn}&format=json&jscmd=data"
            response = requests.get(url)
            
            if response.status_code == 200:
                data = response.json()
                
                if f"ISBN:{isbn}" in data:
                    detalhes = data[f"ISBN:{isbn}"]
                    
                    titulo = detalhes.get('title', 'Título não disponível')
                    autores = detalhes.get('authors', [])
                    autor = ', '.join(author.get('name', 'Autor desconhecido') for author in autores)
                    

                    data_publi_raw = detalhes.get('publish_date', None)
                    if data_publi_raw:
                        try:
                            datetime.strptime(data_publi_raw, '%Y-%m-%d')
                            data_publi = datetime.strptime(data_publi_raw, '%Y-%m-%d').strftime('%d/%m/%Y')
                        except ValueError:
                            try:
                                datetime.strptime(data_publi_raw, '%Y-%m')
                                data_publi = datetime.strptime(data_publi_raw, '%Y-%m').strftime('%m/%Y')
                            except ValueError:
                                data_publi = 'Data de publicação não disponível'
                    else:
                        data_publi = 'Data de publicação não disponível'
                    
                    livro = Livro(
                        titulo=titulo,
                        autor=autor,
                        isbn=isbn,
                        data_publi=data_publi
                    )
                    livro.save()
                    return redirect('livros:listarLivros')
                else:
                    form.add_error('isbn', 'Detalhes do livro não encontrados na API.')
            else:
                form.add_error('isbn', 'Erro ao acessar a API do Open Library.')
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
            return redirect('listaUser')
    else:
        form = UsuarioForm()
    
    return render(request, 'usuarios/formUser.html', {'form': form})

def editarUser(request, usuarioId):
    usuario = get_object_or_404(Usuario, id=usuarioId)
    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('listaUser')
    else:
        form = UsuarioForm(instance=usuario)
    return render(request, 'usuarios/formUser.html', {'form': form})

def excluirUser(request, usuarioId):
    usuario = get_object_or_404(Usuario, id=usuarioId)
    if request.method == 'POST':
        usuario.delete()
        return redirect('listaUser') 
    return render(request, 'usuarios/confirmarExclusao.html', {'usuario': usuario})