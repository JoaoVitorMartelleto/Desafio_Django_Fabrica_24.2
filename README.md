# Catálogo de Leitura

Sistema feito para ter controle sobre quais livros você já leu e avaliá-los. Com esta aplicação, você pode adicionar livros ao seu catálogo pessoal, marcar aqueles que já leu, e avaliar cada livro com notas e comentários.

## Funcionalidades

- **Cadastro de Livros:** Adicione novos livros ao seu catálogo, incluindo detalhes como título, autor, descrição, ISBN, e mais.
- **Controle de Status de Leitura:** Marque livros como "Lido" ou "Não Lido" e filtre sua lista de acordo com o status.
- **Avaliação de Livros:** Dê uma nota aos livros que você leu e adicione comentários para registrar suas impressões.
- **Visualização da Lista de Livros:** Veja todos os livros cadastrados em seu catálogo, com destaque para o status de leitura e nota.
- **Pesquisa e Filtros:** Encontre rapidamente livros por título, autor ou ISBN e filtre a lista por status de leitura ou nota.
  
## Estrutura do Projeto

### Entidades Principais

1. **Livro**
   - **Título:** Nome do livro.
   - **Autor:** Nome do autor ou um relacionamento com a entidade Autor.
   - **Descrição:** Sinopse ou descrição do livro.
   - **ISBN:** Código identificador único.
   - **Status de Leitura:** Indica se o livro foi lido ou não.
   - **Nota:** Nota dada ao livro (por exemplo, de 0 a 5).
   - **Data de Leitura:** Data em que o livro foi lido.
   - **Comentários:** Observações pessoais sobre o livro.

2. **Usuário**
   - **Nome:** Nome do usuário.
   - **Email:** Email do usuário para login e comunicação.
   - **Livros:** Relacionamento entre o usuário e os livros para controle pessoal.

### Principais Funcionalidades

- **Cadastro de Livros:** Formulário para adicionar novos livros ao catálogo.
- **Controle de Status de Leitura:** Marque livros como "Lido" ou "Não Lido".
- **Avaliação de Livros:** Interface para avaliação e comentários sobre os livros.
- **Visualização da Lista de Livros:** Exibição e gerenciamento dos livros cadastrados.
- **Detalhes do Livro:** Página com informações completas sobre o livro.
- **Pesquisa e Filtros:** Funcionalidades de busca e filtragem para facilitar a navegação.

## Tecnologias Utilizadas

- **Django:** Framework utilizado para o desenvolvimento da aplicação.
- **Django Templates:** Para renderização das páginas HTML.
- **Bootstrap:** (ou outro framework CSS) para estilização e responsividade.

## Como Rodar o Projeto

1. Clone este repositório:
```sh
git clone https://github.com/JoaoVitorMartelleto/Desafio_Django_Fabrica_24.2
```
   
2. Crie e ative um ambiente virtual utilizando o venv:

```sh
python -m venv venv
venv/Scripts/activate  # Para Windows
```

3. Caso você enfrente algum erro ao tentar ativar o ambiente virtual, execute o seguinte comando no PowerShell para alterar a política de execução:
```sh
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```
4. Instale as dependências listadas no arquivo requirements.txt:
```sh
pip install -r requirements.txt
```
5. Realize as migrações do banco de dados:
```sh
python manage.py migrate
```
6. Inicie o servidor de desenvolvimento:
```sh
python manage.py runserver
```
Abra a sua IDE de preferência (como PyCharm, VS Code, etc.) para editar o código, realizar melhorias, e monitorar a aplicação.

### Dicas para Utilizar a IDE

- **Importe o projeto para a IDE:**  
  Abra o diretório do projeto na IDE para facilitar a navegação e edição dos arquivos.

- **Utilize a IDE para gerenciar o ambiente virtual:**  
  Algumas IDEs, como PyCharm e VS Code, podem detectar automaticamente e ativar o ambiente virtual, facilitando o desenvolvimento.