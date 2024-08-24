from django import forms
from .models import Livro
from .models import Usuario

class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ['titulo', 'autor', 'isbn', 'data_publi', 'lido', 'nota', 'comentarios']
        
class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['usuario', 'email', 'titulo']