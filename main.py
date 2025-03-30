from function import buscar_livro, cadastar, listar_livros, menu_cadastros, painel

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
        menu_cadastros()
        option = int(input("Digite sua escolha: "))
        if option == 1:
            cadastar("autor", autor)
        elif option == 2:
            cadastar("categoria", categoria)
        elif option == 3:
            cadastar("livro", livro)
    elif option == 2:
        listar_livros()
    elif option == 3:
        buscar_livro()
    elif option == 0:
        isRun = False