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
