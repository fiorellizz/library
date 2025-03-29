from Arquivo import grava_arquivo

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

def painel():
    print("Digite 1 para cadastrar um livro")
    print("Digite 2 para listar todos os livros")
    print("Digite 3 para buscar um livro")
    print("Digite 0 para sair")

def cadastar():
    tituloLivro = input("Digite o título do livro: ")
    anoPublicacaoLivro = int(input("Digite o ano de publicação do livro: "))
    isbnLivro = input("Digite o ISBN do livro: ")

    livro["titulo"] = tituloLivro
    livro["anoPublicacao"] = anoPublicacaoLivro
    livro["ISBN"] = isbnLivro

    grava_arquivo("livro", livro)

isRun = True

while isRun:
    painel()
    option = int(input("Digite sua escolha: "))
    if option == 1:
        cadastar()
    elif option == 2:
        print("Digitou 2")
    elif option == 3:
        print("Digitou 3")
    elif option == 0:
        isRun = False