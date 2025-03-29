def painel():
    print("Digite 1 para cadastrar um livro")
    print("Digite 2 para listar todos os livros")
    print("Digite 3 para buscar um livro")
    print("Digite 0 para sair")

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

livro = {
    "titulo": tituloLivro,
    "autor": autor,
    "anoPublicacao": anoPublicacaoLivro,
    "ISBN": "aAA",
    "categoria": categoria
}

livro2 = {
    "titulo": "Outro",
    "autor": autor,
    "anoPublicacao": 1999,
    "ISBN": "AAAAAAA",
    "categoria": categoria
}


listaLivros = []
listaLivros.append(livro)
listaLivros.append(livro2)
print(listaLivros)

isRun = True

while isRun:
    painel()
    option = int(input("Digite sua escolha: "))
    if option == 1:
        print("Digitou 1")
    elif option == 2:
        print("Digitou 2")
    elif option == 3:
        print("Digitou 3")
    elif option == 0:
        isRun = False