from menu import *

def grava_arquivo(type, dados):
    tipo = type.casefold()
    if tipo == "livro":    
        arquivo = open("biblioteca.csv","a")
 
        arquivo.write(f"{dados}" +"\n")

        arquivo.close()
        return
    elif tipo == "usuario":
        arquivo = open("usuarios.csv","a")

        arquivo.write(f"{dados}" +"\n")

        arquivo.close()
        return
    elif tipo == "emprestimo":
        arquivo = open("emprestimos.csv","a")

        arquivo.write(f"{dados}" +"\n")
        
        arquivo.close()
        return
    elif tipo == "categoria":
        arquivo = open("categorias.csv","a")
        
        arquivo.write(f"{dados}" +"\n")

        arquivo.close()
        return        
    elif tipo == "autor":
        arquivo = open("autor.csv","a")
   
        arquivo.write(f"{dados}" +"\n")
 
        arquivo.close()
        return

#iclusão do metodo para ler o arquivo e realizar a listagem e busca dos dados
def ler_arquivo(type):
    tipo = type.casefold() #CASEFOLD evita o case sensitive para não da erro nas buscas
    nome_arquivo = ""

    # para caso precise utilizar o metodo nos outros arquivos
    if tipo == "livro":
        nome_arquivo = "biblioteca.csv"
    elif tipo == "usuario":
        nome_arquivo = "usuarios.csv"
    elif tipo == "emprestimo":
        nome_arquivo = "emprestimos.csv"
    elif tipo == "categoria":
        nome_arquivo = "categorias.csv"
    elif tipo == "autor":
        nome_arquivo = "autor.csv"
    else:
        print("Tipo de arquivo inválido!")
        return []

    try:
        with open(nome_arquivo, "r") as arquivo:
            linhas = arquivo.readlines()
            dados = [eval(linha.strip()) for linha in linhas]  # Converte string para dicionário
        return dados
    except FileNotFoundError: 
        return []
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")
        return []

def cadastar(data):
    
    menu_cadastros()
    
    option = int(input("Digite sua escolha: "))
    
    if option == 3:
        livro = data
        tituloLivro = input("Digite o título do livro: ")
        anoPublicacaoLivro = int(input("Digite o ano de publicação do livro: "))
        isbnLivro = input("Digite o ISBN do livro: ")

        livro["titulo"] = tituloLivro
        livro["anoPublicacao"] = anoPublicacaoLivro
        livro["ISBN"] = isbnLivro

        autor = input("Digite o autor do livro: ")
        categoria = input("Digite a categoria do livro: ")

        #criar uma função que retorne apenas o dicionario do autor ou do livro de acordo com oq o usuario digitou
        #essa ler_arquivo retorna tudo do arquivo
        autor = ler_arquivo("autor")
        categoria = ler_arquivo("categoria")

        livro["autor"] = autor
        livro["categoria"] = categoria

        try:
            grava_arquivo("livro", livro)
            print("Livro cadastrado com sucesso!")
        except Exception as e:
            print(f"Erro ao cadastrar o livro: {e}")
    
    elif option == 1:
        autor = data
        nomeAutor = input("Digite o nome do autor: ")

        autor["nome"] = nomeAutor

        try:
            grava_arquivo("autor", autor)
            print("Autor cadastrado com sucesso!")
        except Exception as e:
            print(f"Erro ao cadastrar o autor: {e}")

    elif option == 2:
        categoria = data
        nomeCategoria = input("Digite o nome da categoria: ")

        categoria["nome"] = nomeCategoria

        try:
            grava_arquivo("categoria", categoria)
            print("Categoria cadastrada com sucesso!")
        except Exception as e:
            print(f"Erro ao cadastrar a categoria: {e}")

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
        print("\nNenhum livro cadastrado.")
        return

    menu_busca()

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
        print("\nOpção inválida!")
        return

    if resultados:
        print("\nRESULTADOS DA BUSCA")
        for livro in resultados:
            print(f"Título: {livro['titulo']} | Autor: {livro['autor']['nome']} | Ano: {livro['anoPublicacao']} | ISBN: {livro['ISBN']} | Categoria: {livro['categoria']['nome']}")
    else:
        print("\nNenhum livro encontrado!")