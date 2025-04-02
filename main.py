from function import *
from menu import *

autor = {
    "id": 1,
    "nome": "Roberto"
}

categoria = {
    "id": 1,
    "nome": "Romance"
}

tituloLivro = ""
anoPublicacaoLivro = 0
isbnLivro = ""

livro = {
    "titulo": tituloLivro,
    "autor": autor,
    "anoPublicacao": anoPublicacaoLivro,
    "ISBN": isbnLivro,
    "categoria": categoria
}

listaLivros = []

isRun = True

while isRun:
    painel()
    option = int(input("Digite sua escolha: "))
    if option == 1:
        cadastar()
    elif option == 2:
        listar_livros()
    elif option == 3:
        buscar_livro()
    elif option == 0:
        isRun = False