from Arquivo import grava_arquivo, ler_arquivo

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
    print("\n======== Biblioteca Virtual ========")
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

#inclusão do método listar
def listar_livros():
    livros = ler_arquivo("livro")

    if not livros:
        print("Nenhum livro cadastrado.")
        return

    print("\nLISTA DE LIVROS")
    for livro in livros:
        print(f"Título: {livro['titulo']} | Autor: {livro['autor']['nome']} | Ano: {livro['anoPublicacao']} | ISBN: {livro['ISBN']} | Categoria: {livro['categoria']['nome']}")

#inclusão do método buscar por título, autor ou categoria
def buscar_livro():
    livros = ler_arquivo("livro")

    if not livros:
        print("Nenhum livro cadastrado.")
        return

    print("\nBuscar Livro")
    print("1 - Buscar por Título")
    print("2 - Buscar por Autor")
    print("3 - Buscar por Categoria")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        valor = input("Digite o título: ").lower() #esse lower faz com que todas as strings retornem minusculas para não dar erro
        resultados = [livro for livro in livros if valor in livro['titulo'].lower()]
    elif opcao == "2":
        valor = input("Digite o nome do autor: ").lower()
        resultados = [livro for livro in livros if valor in livro['autor']['nome'].lower()]
    elif opcao == "3":
        valor = input("Digite a categoria: ").lower()
        resultados = [livro for livro in livros if valor in livro['categoria']['nome'].lower()]
    else:
        print("Opção inválida!")
        return

    if resultados:
        print("\nRESULTADOS DA BUSCA")
        for livro in resultados:
            print(f"Título: {livro['titulo']} | Autor: {livro['autor']['nome']} | Ano: {livro['anoPublicacao']} | ISBN: {livro['ISBN']} | Categoria: {livro['categoria']['nome']}")
    else:
        print("Nenhum livro encontrado!")

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