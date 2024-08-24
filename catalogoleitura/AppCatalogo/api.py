
import requests

def obter_detalhes_livro(isbn):
    url = f"https://openlibrary.org/api/books?bibkeys=ISBN:{isbn}&format=json&jscmd=data"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if f"ISBN:{isbn}" in data:
            detalhes = data[f"ISBN:{isbn}"]
            return {
                'title': detalhes.get('title', ''),
                'authors': [{'name': author.get('name')} for author in detalhes.get('authors', [])],
                'publish_date': detalhes.get('publish_date', None),
                'description': detalhes.get('description', ''),
            }
    return None
